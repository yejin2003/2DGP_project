# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import load_image
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDL_KEYUP


def space_down(e):
    return e[0]=='INPUT' and e[1].type==SDL_KEYDOWN and e[1].key==SDLK_SPACE

class Run:
    @staticmethod
    def enter(prince):
        prince.dir, prince.action=1
    @staticmethod
    def exit(prince,e):
        pass

    @staticmethod
    def do(prince):
        prince.frame=(prince.frame+1)%10
        prince.x+=prince.dir*5
        pass

    @staticmethod
    def draw(prince):
        prince.image.clip.draw(prince.frame*100,100,100,prince.x,prince.y)


class Jump:
    @staticmethod
    def enter(prince,e):
        if space_down(e):
            prince.dir,prince.action=1,1

    @staticmethod
    def exit(prince, e):
        pass

    @staticmethod
    def do(prince):
        prince.frame=(prince.frame+1)%10
        prince.x+=prince.dir*5
        pass

    @staticmethod
    def draw(prince, e):
        prince.image.clip_draw(prince.frame*100,prince.action*100,100,100,prince.x,prince.y)

class Skill:
    pass



class StateMachine:
    def __init__(self,prince):
        self.prince= prince
        self.cur_state=Run
        self.transitions={
            Run:{space_down:Jump}
        }

    def start(self):
        self.cur_state.enter(self.prince)

    def update(self):
        self.cur_state.do(self.prince)


    def draw(self):
        self.cur_state.draw(self.prince)

    def handle_event(self,e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.prince)
                self.cur_state=next_state
                self.cur_state.enter(self.prince)
                return True
        return False




class Prince:
    def __init__(self, ):
        self.x, self.y = 400, 90
        self.frame = 0
        self.action = 0
        self.image = load_image('prince_run_animation.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT',event))
        pass

    def draw(self):
        self.state_machine.draw()
