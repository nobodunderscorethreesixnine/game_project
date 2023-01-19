import pygame
import threading
import socket

pygame.init()
# pygame variable
WIDTH , HEIGHT = 900 , 600
win = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("player_1")

# connecting to server , socket variable
server_ip , server_port = "192.168.1.68" , 9999
client = socket.socket()
client.connect((server_ip , server_port))

# player 2 image
player_2_paper_image = pygame.image.load('images_for_SPR/player_2_hand.png')
player_2_rock_image = pygame.image.load('images_for_SPR/player_2_rock.png')
player_2_scissor_image = pygame.image.load('images_for_SPR/player_2_scissor.png')

def hello(data):
    if data == 'scissor':
        win.blit(player_2_scissor_image , (595 , 20))
    elif data == 'paper':
        win.blit(player_2_paper_image , (595 , 20))
    elif data == 'rock':
        win.blit(player_2_rock_image , (595 , 20))


def recv_message():
    while True:
        data = client.recv(1024)
        print(data.decode("utf-8"))
        hello(data.decode())
# def send_message():
#     while True:
#         message = input('enter message: ')
#         client.send(message.encode('utf-8'))
#         thread = threading.Thread(target=recv_message)
#         thread.start()

# send_message()
thread_starter = True
if thread_starter:
    thread = threading.Thread(target=recv_message)
    thread.start()
elif thread_starter == False:
    exit()
# pygame variable

WIDTH , HEIGHT = 900 , 600
win = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("player_1")

def drawing_buttons():
    global rock_button , paper_button , scissor_button
    font_type = pygame.font.SysFont('monospace' , 29)
    weapons = ["rock" , "paper" , "scissor"]
    width = 130
    height = 40
    x_pos = 20
    y_pos = 299
    thickness = 3
    text_color = 'red'
    button_color = "yellow"     
    # drawing rock button and text
    rock_button = pygame.draw.rect(win , button_color , (x_pos , y_pos , width , height), thickness)
    text_inside_rock_button = font_type.render('rock' , 1 , text_color)
    win.blit(text_inside_rock_button , (x_pos + 10 , y_pos + 5))

#    drawing paper button and text
    x_pos += 150
    paper_button = pygame.draw.rect(win , button_color , (x_pos , y_pos, width , height) , thickness)
    text_inside_paper_button = font_type.render('paper' , 1, text_color)
    win.blit(text_inside_paper_button , (x_pos +10 , y_pos + 5))

#    drawing scissor button and text
    x_pos += 150
    scissor_button = pygame.draw.rect(win , button_color , (x_pos , y_pos , width , height) , thickness)
    text_inside_scissor_button = font_type.render('scissor' , 1, text_color)
    win.blit(text_inside_scissor_button , (x_pos + 7 , y_pos + 5))


# loading images of rock , paper , scissor
player_1_paper_image = pygame.image.load('images_for_SPR/player_1_hand.png')
player_1_rock_image = pygame.image.load('images_for_SPR/player_1_rock.png')
player_1_scissor_image = pygame.image.load('images_for_SPR/player_1_scissor.png')



def click_checker(m_x_pos , m_y_pos):
    global button_tracker
    if (m_x_pos > rock_button.left) and (m_x_pos < rock_button.right) and (m_y_pos < rock_button.bottom) and (m_y_pos > rock_button.top):        
        print("clicked rock")
        client.send(b"rock")
        win.blit(player_1_rock_image  ,(30,10))
    elif (m_x_pos > paper_button.left) and (m_x_pos < paper_button.right) and (m_y_pos < paper_button.bottom) and (m_y_pos > paper_button.top):
        print("clicked paper")
        client.send(b"paper")
        win.blit(player_1_paper_image , (30,10))
    elif (m_x_pos > scissor_button.left) and (m_x_pos < scissor_button.right) and (m_y_pos < scissor_button.bottom) and (m_y_pos > scissor_button.top):
        print("clicked scissor")
        client.send(b"scissor")
        win.blit(player_1_scissor_image,(30,10))

def main():
    global thread_starter
    RUN = True    
    win.fill("black")
    drawing_buttons()
    while RUN:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x_pos , m_y_pos = pygame.mouse.get_pos()
                click_checker(m_x_pos , m_y_pos)
        pygame.display.update()       
    thread_starter = False
    pygame.quit()
    
    


main()
