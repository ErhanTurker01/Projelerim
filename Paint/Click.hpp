//
//  Click.hpp
//  WorldEditor
//
//  Created by Erhan Türker on 6/18/23.
//
#include <iostream>
#include <SDL2/SDL.h>
#ifndef Click_hpp
#define Click_hpp
class ClickObject{
public:
    SDL_Rect *rect;
    SDL_Surface *surface;
    ClickObject(SDL_Rect *rectt, SDL_Surface *surface):surface(surface)
    {rect=(SDL_Rect*)malloc(sizeof(SDL_Rect));rect->w=rectt->w;rect->h=rectt->h;rect->x=rectt->x;rect->y=rectt->y;}
    ClickObject(){rect=NULL;surface=NULL;}
    bool isClicked(int x, int y){return (rect->x<=x && rect->x+rect->w>=x) && (rect->y<=y && rect->y+rect->h>=y);}
    
};

class Panel : public ClickObject{
public:
    ClickObject ocButton;
    std::vector<ClickObject> elements;
    bool open;
};

#endif /* Click_hpp */
