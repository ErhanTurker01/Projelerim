/*
 * Screen.cpp
 *
 *  Created on: 26 Şub 2023
 *      Author: erhanturker
 */

#include "Screen.h"
using namespace std;

namespace Erhan {

Screen::Screen() :
		screenColor(0x00000000) {
}

Screen::Screen(unsigned int screenColor) :
		screenColor(screenColor) {
}

void Screen::setPixel(int x, int y, unsigned int color) {
	buffer[x + y * WIDTH] = color;
}


void Screen::drawRectangle(int x, int y, int width, int height,
		unsigned int color) {

	for (int j = y; j < y + height; j++) {
		for (int i = x; i < x + width; i++) {
			setPixel(i, j, color);
		}
	}
}


void Screen::drawCircle(int x, int y, int r, unsigned int color) {
	for (int j = y - r; j < y + r; j++) {
		for (int i = x - r; i < x + r; i++) {
			if ((x - i) * (x - i) + (y - j) * (y - j) < r * r) {
				setPixel(i, j, color);
			}
		}
	}
}


void Screen::update() {
	SDL_UpdateTexture(texture, NULL, buffer, WIDTH * sizeof(Uint32));
	SDL_RenderClear(renderer);
	SDL_RenderCopy(renderer, texture, NULL, NULL);
	SDL_RenderPresent(renderer);
	drawRectangle(0, 0, WIDTH, HEIGHT, screenColor);
}

void Screen::update(unsigned int color) {
	SDL_UpdateTexture(texture, NULL, buffer, WIDTH * sizeof(Uint32));
	SDL_RenderClear(renderer);
	SDL_RenderCopy(renderer, texture, NULL, NULL);
	SDL_RenderPresent(renderer);
	drawRectangle(0, 0, WIDTH, HEIGHT, color);
}

bool Screen::init() {
	if (SDL_Init(SDL_INIT_VIDEO) < 0) {
		cout << "fail" << endl;
		return false;
	}

	window = SDL_CreateWindow("Window", SDL_WINDOWPOS_UNDEFINED,
	SDL_WINDOWPOS_UNDEFINED, WIDTH, HEIGHT, 1);
	;
	if (window == NULL) {
		SDL_Quit();
		cout << "could not create window" << endl;
		return false;
	}

	renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_PRESENTVSYNC);
	if (renderer == NULL) {
		cout << "could not create renderer" << endl;
		SDL_DestroyWindow(window);
		SDL_Quit();
		return false;
	}

	texture = SDL_CreateTexture(renderer, SDL_PIXELFORMAT_RGBA8888,
			SDL_TEXTUREACCESS_STATIC, WIDTH, HEIGHT);
	if (texture == NULL) {
		cout << "could not create texture" << endl;
		SDL_DestroyRenderer(renderer);
		SDL_DestroyWindow(window);
		SDL_Quit();
		return false;
	}

	buffer = new Uint32[WIDTH * HEIGHT];

	for (int i = 0; i < WIDTH * HEIGHT; i++) {
		buffer[i] = screenColor;
	}

	return true;
}

void Screen::close() {
	delete[] buffer;
	SDL_DestroyTexture(texture);
	SDL_DestroyRenderer(renderer);
	SDL_DestroyWindow(window);
	SDL_Quit();
}

bool Screen::processEvents() {
	SDL_Event event;
	while (SDL_PollEvent(&event)) {
		if (event.type == SDL_QUIT) {
			return false;
		}
	}
	return true;
}

}
