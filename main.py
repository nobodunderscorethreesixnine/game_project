import threading
import socket
import pygame
pygame.init()

WIDTH , HEIGHT = 900 , 600
win = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("SPR_player1")


##server.listen(1) #backlog
##print("waiting for connection")
##
##client_info , addr = server.accept()
##print("client connected" , addr)
##client_handler = threading.Thread(target=client)
##client_handler.start()


ip , port = "localhost" , 1234
server = socket.socket()
server.bind((ip , port))
server.listen()

def networking():
    global request
    while True:
        client , address = server.accept()
        print(f"connected to {address}")
        request = client.recv(1024)
        print(request)
        
##        print(request.decode())
        


client_handler = threading.Thread(target=networking)
client_handler.start()
##print(request.  decode()) #start from *
# search in internet how to get return value from thread in python





        

# start form here make multithreaded server to listen the client *remember
#checking who win will be in different file server.py make logic *excetue
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


player_1_paper_image = pygame.image.load('images_for_SPR/player_1_hand.png')
player_1_rock_image = pygame.image.load('images_for_SPR/player_1_rock.png')
player_1_scissor_image = pygame.image.load('images_for_SPR/player_1_scissor.png')


# start form here * try to make blur around image(rock ,paper etc) until user click button make it real 
def click_checker(m_x_pos , m_y_pos):
    global button_tracker
    if (m_x_pos > rock_button.left) and (m_x_pos < rock_button.right) and (m_y_pos < rock_button.bottom) and (m_y_pos > rock_button.top):        
        print("clicked rock")
        win.blit(player_1_rock_image  ,(30,10))
    elif (m_x_pos > paper_button.left) and (m_x_pos < paper_button.right) and (m_y_pos < paper_button.bottom) and (m_y_pos > paper_button.top):
        print("clicked paper")
        win.blit(player_1_paper_image , (30,10))
    elif (m_x_pos > scissor_button.left) and (m_x_pos < scissor_button.right) and (m_y_pos < scissor_button.bottom) and (m_y_pos > scissor_button.top):
        print("clicked scissor")
        win.blit(player_1_scissor_image,(30,10))

##def drawing_image():
##    if button_tracker == 'paper':
##        image = pygame.image.load('images_for_SPR/player_1_hand.png')
##        image2 = pygame.image.load('images_for_SPR/player_2_hand.png')
##    elif button_tracker == 'rock':
##        image = pygame.image.load('images_for_SPR/player_1_rock.png')
##        image2 = pygame.image.load('images_for_SPR/player_2_rock.png')
##    else:
##        image = pygame.image.load('images_for_SPR/player_1_scissor.png')
##        image2 = pygame.image.load('images_for_SPR/player_2_scissor.png')
##
##    
##    win.blit(image , (0 , 0))
##    win.blit(image2 , (500  , 0))
    
    


def main():    
    global button_tracker 
    RUN = True    
    win.fill('black')    
    drawing_buttons()
    
##    if request.decode() == "scissor":
##        win.blit(player_1_paper_image , (500 , 0))
    
    
    while RUN:
        button_tracker = ''
##        print(button_tracker)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                m_x_pos , m_y_pos = pygame.mouse.get_pos()
                click_checker(m_x_pos , m_y_pos)                
        pygame.display.update()
    pygame.quit()                



##x = threading.Thread(target=main)
##x.start()
##networking()
##client_handler.start()   
main()

