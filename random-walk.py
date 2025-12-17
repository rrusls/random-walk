WIDTH= 900
HEIGHT = 600
import random
import sdl3
import ctypes
import sdl3.SDL_events
import colorsys
    
window = sdl3.SDL_CreateWindow("Test".encode(),WIDTH,HEIGHT,0)
renderer = sdl3.SDL_CreateRenderer(window,None)
wsurface = sdl3.SDL_GetWindowSurface(window)
SCALE = 10

#Uint32 used in SDL_FillSurfaceRect(), HSL to make it bright colors only
def hlscol():
    h = random.random()
    s = 1
    l = 0.5
    r,g,b = colorsys.hls_to_rgb(h,l,s)

    r,g,b = int(r*255), int(g*255), int(b*255)
    a = 255
    return (a << 24) | (r << 16) | (g << 8) | b

#def rgbtouint32(r,g,b): <- Uint32 to rgb (can be used if you don't care about the color's brightness)
    #a = 255
    #return (a << 24) | (r << 16) | (g << 8) | b


#Randomize the directions for agents where N = amount of agents
N = int(input("Number of agents: "))
agents = [[WIDTH//2,HEIGHT//2,0,0,hlscol()] for _ in range(N)]
DIR = [(0,-1),(0,1),(-1,0),(1,0)]
def randomize_directions(agents):
    for _ in range(N):
        agents[_][2],agents[_][3] = random.choice(DIR)
    return agents




#Agent
agent = sdl3.SDL_FRect(WIDTH//2,HEIGHT//2,2.0,2.0)

#init
running = True
event = sdl3.SDL_Event()
while running:
    while sdl3.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl3.SDL_events.SDL_EVENT_QUIT:
            running = 0
    #sdl3.SDL_SetRenderDrawColor(renderer,0,0,0,0)#sdl3.SDL_ALPHA_OPAQUE)

    #rect
    sdl3.SDL_SetRenderDrawColor(renderer,0,0,0,sdl3.SDL_ALPHA_OPAQUE)

    
    
    for i in range(N):
        agents = randomize_directions(agents)
        x,y,dx,dy,uint32_col = agents[i]
        for _ in range(SCALE):
            x += dx
            y += dy 
            agent = sdl3.SDL_Rect(x,y,2,2,)
            sdl3.SDL_FillSurfaceRect(wsurface,agent,uint32_col) #0xFFFFFF -> (r, g, b)
        agents[i][0],agents[i][1] = x,y
       
    sdl3.SDL_UpdateWindowSurface(window)
    sdl3.SDL_Delay(20)


sdl3.SDL_DestroyRenderer(renderer)
sdl3.SDL_DestroyWindow(window)
sdl3.SDL_Quit()





