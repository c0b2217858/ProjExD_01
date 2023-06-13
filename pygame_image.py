import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)

    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_img = pg.transform.rotate(kk_img,10)
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img,10,1.0)]
    tmr = 0
    x = 0
    y = 0
    z = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return


        if(x == 1600):
            x = 0
        
        if(y):
            z -= 1
        else:
            z += 1
        
        if(z > 100):
            y = 1
        elif(z< -100):
            y = 0


        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(kk_imgs[y],[300,200])
        pg.display.update()
        tmr += 1
        x += 1        
        clock.tick(500)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()