#include <iostream>
#include <vector>
#include <algorithm>
#include <dirent.h>
#include <SDL2/SDL.h>
#include <SDL2_image/SDL_image.h>
#include "Click.hpp"







using std::cout,std::endl,std::vector;

const int PIXEL=16,WIDTH=40,HEIGHT=30;
bool running = true;
bool holdingMouse1 = false;
bool holdingMouse2 = false;
bool drawingMode = false;
bool deletingMode = false;
bool freeMode = true;
bool UIhide = false;
short scroll = 0;



enum surfaces{
    whites,
    crosss,
    blacks
};

vector<SDL_Surface*> loadSurfaces(vector<std::string> surfaceNames,SDL_Window* window);
vector<SDL_Surface*> loadDefaultSurfaces(vector<std::string> surfaceNames,SDL_Window* window);
void blitClickObjectSurfaces(vector<ClickObject> objects ,SDL_Surface *windowSurface);
void mouseClick(SDL_Event event);
void drawBlock(int x, int y, SDL_Surface *surface);
bool isInPanel(Panel panel, int x, int y);


SDL_Surface *windowSurface=nullptr;
SDL_Surface *selectedSurface=nullptr;
ClickObject drawnSurfaces[WIDTH][HEIGHT];





int main(){
    vector<std::string> surfaceNames;
    vector<std::string> defaultSurfaceNames;
    DIR *dir;
    struct dirent *ent;
    if ((dir = opendir ("default")) != NULL) {
      while ((ent = readdir (dir)) != NULL) {
          if (ent->d_name[0] != '.') defaultSurfaceNames.push_back(ent->d_name);
      }
      closedir (dir);
    } else {
      perror ("");
      return 1;
        
    }if ((dir = opendir ("surfaces")) != NULL) {
      while ((ent = readdir (dir)) != NULL) {
          if (ent->d_name[0] != '.') surfaceNames.push_back(ent->d_name);
      }
      closedir (dir);
    } else {
      perror ("");
      return 1;
    }
    
    std::sort(surfaceNames.begin(), surfaceNames.end(), [](std::string a, std::string b){return a>b;});
    std::sort(defaultSurfaceNames.begin(), defaultSurfaceNames.end(), [](std::string a, std::string b){return a>b;});
    
    
    if(SDL_Init(SDL_INIT_EVERYTHING) < 0 && ( !( IMG_Init( IMG_INIT_PNG ) & IMG_INIT_PNG ) )){
        cout << "SDL could not be initialized: " << SDL_GetError() << endl;
        running = false;
    }else{
        cout << "SDL video system is ready to go\n" << endl;
    }
    
    SDL_Window* window=nullptr;
    window = SDL_CreateWindow("Deneme", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, WIDTH*PIXEL, HEIGHT*PIXEL, SDL_WINDOW_SHOWN);
    if(window == NULL){
        std::cout << "SDL window not be initialized: " << SDL_GetError() << endl;
        running = false;
    }

    
    
    vector<SDL_Surface*> dSurface = loadDefaultSurfaces(defaultSurfaceNames,window);
    vector<SDL_Surface*> surface = loadSurfaces(surfaceNames,window);
    Panel panel;
    Panel colorPanel;
    SDL_Rect tempRect;
    for (auto name : defaultSurfaceNames) {
        cout << name << endl;
    }
    if (running) {
        panel.rect = (SDL_Rect*)malloc(sizeof(SDL_Rect));
        tempRect.x = PIXEL*3.5;
        tempRect.y = PIXEL;
        tempRect.w = PIXEL;
        tempRect.h = PIXEL;
        panel.ocButton = ClickObject(&tempRect,dSurface[crosss]);
        tempRect.y=PIXEL*1.5;
        tempRect.x=PIXEL/2;
        for (int i=0; i<surface.size(); i++) {
            if(i%2) tempRect.x = PIXEL*2.25;
            else {tempRect.y += (int)((float)PIXEL*(1.25)); tempRect.x = PIXEL;}
            panel.elements.push_back(ClickObject(&tempRect,surface[i]));
        }
        panel.rect->y = 0;
        panel.rect->x = 0;
        panel.rect->w = PIXEL*4;
        panel.rect->h = panel.elements[panel.elements.size()-1].rect->y+PIXEL*2;
        
        
        tempRect.x=WIDTH*PIXEL-50;
        tempRect.y=20;
        colorPanel.ocButton = ClickObject(&tempRect,dSurface[crosss]);
        tempRect.y=30;
        tempRect.x-=30;
        colorPanel.elements.push_back(ClickObject(&tempRect, dSurface[blacks]));
        tempRect.x-=30;
        colorPanel.elements.push_back(ClickObject(&tempRect, dSurface[blacks]));
        tempRect.x-=30;
        colorPanel.elements.push_back(ClickObject(&tempRect, dSurface[blacks]));
    }
    int bgColor=0xffffffff;
    SDL_Event event;
    while(running){
        if(SDL_PollEvent(&event)){
            if(event.type == SDL_QUIT){
                running = false;
            }
            if (event.type==SDL_KEYDOWN) {
                
                if (event.key.keysym.sym == SDLK_h) UIhide = !UIhide;
                if (event.key.keysym.sym == SDLK_ESCAPE) running = false;
                if (event.key.keysym.sym == SDLK_b) panel.open = true;
                if (event.key.keysym.sym == SDLK_m) colorPanel.open = true;
                if (event.key.keysym.sym == SDLK_d) {drawingMode = true; deletingMode = false; freeMode = false;}
                if (event.key.keysym.sym == SDLK_e) {deletingMode = true; drawingMode = false; freeMode = false;}
                if (event.key.keysym.sym == SDLK_f) {freeMode = true; drawingMode = false; deletingMode = false;}
            }
            
            
            if(event.wheel.type == SDL_MOUSEWHEEL){
                int x,y;
                SDL_GetMouseState(&x, &y);
                if (event.wheel.y < 0 && panel.isClicked(x, y) && panel.open && !UIhide) scroll = -5;
                if (event.wheel.y > 0 && panel.isClicked(x, y) && panel.open && !UIhide) scroll = 5;
            }else scroll = 0;
            mouseClick(event);
            if (holdingMouse1) {
                int x,y;
                SDL_GetMouseState(&x, &y);
                
                if (drawingMode && drawnSurfaces[x/PIXEL][y/PIXEL].surface != selectedSurface && (!panel.isClicked(x, y) || UIhide || !panel.open)) drawBlock(x,y,selectedSurface);
                if(deletingMode&& (!panel.isClicked(x, y) || UIhide || !panel.open)){
                    if(drawnSurfaces[x/PIXEL][y/PIXEL].rect != NULL) {
                        delete drawnSurfaces[x/PIXEL][y/PIXEL].rect;
                        drawnSurfaces[x/PIXEL][y/PIXEL].rect=NULL;
                    }
                    drawnSurfaces[x/PIXEL][y/PIXEL].surface=NULL;
                }
                if(freeMode && !drawingMode && !deletingMode){
                    for (int i=0; i<3; i++) {
                        if (colorPanel.elements[i].isClicked(x, y)) {
                            if (y<40) colorPanel.elements[i].rect->y=30;
                            else if (y>295)colorPanel.elements[i].rect->y=285;
                            else colorPanel.elements[i].rect->y=y-10;
                            cout << -colorPanel.elements[i].rect->y + 285  << endl;
                        }
                    }
                }
                if (colorPanel.ocButton.isClicked(x, y) && !UIhide) colorPanel.open = false;
                if (panel.ocButton.isClicked(x, y) && !UIhide)panel.open = false;
                if (panel.open && !UIhide) {
                    for(auto block : panel.elements){
                        if (block.isClicked(x, y)) {
                            selectedSurface = block.surface;
                            holdingMouse1=false;
                            drawingMode=true;
                            deletingMode=false;
                        }
                    }
                }
            }
        }else scroll = 0;
        bgColor = (((-colorPanel.elements[2].rect->y+285)<<16) + ((-colorPanel.elements[1].rect->y+285)<<8) + (-colorPanel.elements[0].rect->y+285));
        //        Drawing
        SDL_FillRect(windowSurface, NULL, bgColor);
        for (int i = 0; i<WIDTH; i++) {
            for (int j = 0; j<HEIGHT; j++) {
                if (drawnSurfaces[i][j].surface != NULL) {
                    SDL_BlitSurface(drawnSurfaces[i][j].surface,NULL,windowSurface,drawnSurfaces[i][j].rect);
                }
            }
        }
        if (drawingMode) {
            SDL_GetMouseState(&(tempRect.x), &(tempRect.y));
            tempRect.x-=tempRect.x%PIXEL;
            tempRect.y-=tempRect.y%PIXEL;
            SDL_BlitSurface(selectedSurface,NULL,windowSurface,&tempRect);
        }
    
        if (panel.open && !UIhide) for(int i=0; i<panel.elements.size();i++) panel.elements[i].rect->y+=scroll;
        if (!UIhide && panel.open) SDL_BlitSurface(panel.ocButton.surface,NULL,windowSurface,panel.ocButton.rect);
        if (!UIhide && colorPanel.open) SDL_BlitSurface(colorPanel.ocButton.surface,NULL,windowSurface,colorPanel.ocButton.rect);
        if (panel.open && !UIhide) blitClickObjectSurfaces(panel.elements, windowSurface);
        if (!UIhide && colorPanel.open) blitClickObjectSurfaces(colorPanel.elements, windowSurface);
        SDL_UpdateWindowSurface(window);
        SDL_Delay(5);
    }
    
    
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}

vector<SDL_Surface*> loadSurfaces(vector<std::string> surfaceNames,SDL_Window* window){
    vector<SDL_Surface*> surfaceVector = vector<SDL_Surface*>();
    windowSurface = SDL_GetWindowSurface(window);
    int i=0;
    for (auto name : surfaceNames) {
        surfaceVector.push_back(SDL_LoadBMP(&("surfaces/" + name)[0]));
        if (surfaceVector[i] == NULL) {
            running = false;
            break;
        }
        i++;
    }
    return surfaceVector;
}

vector<SDL_Surface*> loadDefaultSurfaces(vector<std::string> surfaceNames,SDL_Window* window){
    vector<SDL_Surface*> surfaceVector = vector<SDL_Surface*>();
    windowSurface = SDL_GetWindowSurface(window);
    int i=0;
    for (auto name : surfaceNames) {
        surfaceVector.push_back(SDL_LoadBMP(&("default/" + name)[0]));
        if (surfaceVector[i] == NULL) {
            running = false;
            break;
        }
        i++;
    }
    return surfaceVector;
}

void blitClickObjectSurfaces(vector<ClickObject> objects,SDL_Surface *windowSurface){
    for (ClickObject object : objects) {
        if (object.rect->y>=0 && object.rect->y<=PIXEL*HEIGHT) SDL_BlitSurface(object.surface,NULL,windowSurface,object.rect);
    }
}

void mouseClick(SDL_Event event){
    if (event.button.type == SDL_MOUSEBUTTONDOWN && event.button.button == SDL_BUTTON_LEFT) holdingMouse1 = true;
    if (event.button.type == SDL_MOUSEBUTTONUP && event.button.button == SDL_BUTTON_LEFT) holdingMouse1 = false;
    if (event.button.type == SDL_MOUSEBUTTONDOWN && event.button.button == SDL_BUTTON_RIGHT) holdingMouse2 = true;
    if (event.button.type == SDL_MOUSEBUTTONUP && event.button.button == SDL_BUTTON_RIGHT) holdingMouse2 = false;
}

void drawBlock(int x, int y, SDL_Surface *surface){
    drawnSurfaces[x/PIXEL][y/PIXEL].rect = (SDL_Rect*)malloc(sizeof(SDL_Rect));
    drawnSurfaces[x/PIXEL][y/PIXEL].rect->x = x-x%PIXEL;
    drawnSurfaces[x/PIXEL][y/PIXEL].rect->y = y-y%PIXEL;
    drawnSurfaces[x/PIXEL][y/PIXEL].rect->w = PIXEL;
    drawnSurfaces[x/PIXEL][y/PIXEL].rect->h = PIXEL;
    drawnSurfaces[x/PIXEL][y/PIXEL].surface = surface;
}

bool isInPanel(Panel panel, int x, int y){
    return (panel.rect->x<=x && panel.rect->x+panel.rect->w>=x) && (panel.rect->y<=y && panel.rect->y+panel.rect->h>=y);
}
