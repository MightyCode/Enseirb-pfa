import numpy as np

EMPTY = 0
SNAKE = 1
APPLE = 2
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class snake:
    def __init__(self, nb_rows, nb_columns, nb_apples) -> None:
        
        self.matrix = np.zeros(nb_rows, nb_columns)
        
        snake_init_head = (np.random.randint(1, nb_rows-1), np.random.randint(1,nb_columns-1)) #init du snake head hors de la bordure pour éviter le spawnkill
        self.snake = (snake_init_head)
        self.matrix[snake_init_head[0], snake_init_head[1]] = SNAKE
        
        
        
        for i in range(nb_apples):
            apple = snake_init_head
            while(apple == snake_init_head):
                apple = (np.random.randint(nb_rows), np.random.randint(nb_columns))
            self.matrix[apple[0], apple[1]]=APPLE
            
        self.direction = np.random.randint(4)
        
        self.win = 0 #0 si partie en cours, 1 si partie terminée et gagnée
        self.lost = 0 #0 si partie en cours, 1 si crash 

        
        
            
    
    #fonctions de voisinnage sur des tableaux de coordonnées
    def up_neighbor(box):
        return ((box[0]-1, box[1]))
    def right_neighbor(box):
        return ((box[0], box[1]+1))
    def down_neighbor(box):
        return ((box[0]+1, box[1]))
    def left_neighbor(box):
        return ((box[0], box[1]-1))
        
        
    def snake_head(self):
        return self.snake[0]
    def snake_tail(self):
        return self.snake[len(self.snake)-1]
    
    def is_apple(self, box):
        return self.matrix[box[0],box[1]]==APPLE
    def add_random_apple(self):
        new_apple = (np.random.randint(self.nb_rows), np.random.randint(self.nb_columns))
        while (self.matrix[new_apple[0], new_apple[1]] != EMPTY) :
            new_apple = (np.random.randint(self.nb_rows), np.random.randint(self.nb_columns))
        self.matrix[new_apple[0], new_apple[1]] = APPLE

    
    def update_direction(self, new_dir):
        self.direction = new_dir
        
    #fait avancer le snake d'une case, agrandit le snake si il y a une pomme dans la case où on veut avancer, et ajoute une pomme si on en mange une
    def update_snake(self, new_box):
        self.snake.insert(0, new_box)
        self.matrix[new_box[0], new_box[1]]=SNAKE
        if(not self.is_apple(self, new_box)):
            tail = self.snake_tail(self)
            self.matrix[tail[0], tail[1]]=EMPTY
            self.snake.pop()
        else:
            self.add_random_apple(self)
        
        
    def is_accessible(self, box):
        if self.matrix[box[0], box[1]]== SNAKE:
            return False
        if box[0]<0 or box[0]>=self.nb_rows or box[1]<0 or box[1]>=self.nb_columns:
            return False
        return True
                
    def update_frame(self, direction):
        if(self.win==0 and self.lost==0):
            head = self.snake_head(self)
            if(direction == UP):
                new_box = self.up_neighbor(head)
            elif(direction == RIGHT):
                new_box = self.right_neighbor(head)
            elif(direction == DOWN):
                new_box = self.down_neighbor(head)
            elif(direction == LEFT):
                new_box = self.left_neighbor(head)
            else:
                raise Exception("La direction n'est pas valide")
            
            if self.is_accessible(self, new_box):
                self.update_snake(self, new_box)
            elif (len(self.snake) == self.nb_rows * self.nb_columns):
                self.win = 1
            else:
                self.lost = 1
                
            
                
