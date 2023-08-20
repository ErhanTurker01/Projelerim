/*
 * Screen.h
 *
 *  Created on: 26 Şub 2023
 *      Author: erhanturker
 */

#ifndef SCREEN_H_
#define SCREEN_H_
#include <iostream>
#include <SDL2/SDL.h>
#include <math.h>

namespace Erhan {

class Screen {
public:
	const static int WIDTH = 1280;
	const static int HEIGHT = 800;

public:
	unsigned int screenColor;
	SDL_Window *window;
	SDL_Renderer *renderer;
	SDL_Texture *texture;
	Uint32 *buffer;

public:
	bool init();
	void close();
	bool processEvents();
	void update();
	void update(unsigned int color);
	void setPixel(int x, int y, unsigned int color);
	void drawRectangle(int x, int y, int width, int height, unsigned int color);
	void drawCircle(int x, int y, int r, unsigned int color);
	Screen();
	Screen(unsigned int screenColor);
};

} /* namespace erh */

#endif /* SCREEN_H_ */
