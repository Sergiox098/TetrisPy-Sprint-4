import pygame
import random
import sys

WIDTH, HEIGHT = 1200, 650 
GRID_SIZE = 30
GRID_WIDTH = 780  
INFO_WIDTH = WIDTH - GRID_WIDTH
COLUMNS = GRID_WIDTH // GRID_SIZE
ROWS = HEIGHT // GRID_SIZE
MAX_ERRORS = 3  
BASE_FALL_SPEED = 1000 
SPEED_INCREASE_PER_LEVEL = 50  
LEVEL_MESSAGE_DURATION = 3000 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
DARK_BG = (30, 30, 30)

FONT_PATH = "PressStart2P-Regular.ttf"


def level_to_string(level_code):
    result = ""
    for word in level_code:
        if word == "/n":
            result += "\n"
        else:
            result += word
    return result

LEVELS = [
    ["print", "(", "\"", "Hola", "mundo", "\"", ")"],
    ["variable", "=", "(", "\"", "Hola", "mundo", "\"", ")"],
    ["edad", "=", "int", "(", "input", "(", "\"", "años", "\"", ")", ")"],
    ["if", "edad", ">=", "18", ":", "/n", "print", "(", "\"", "mayor", "\""],
    ["print", "(", "python", ".", "upper", "(", ")", ")"],
    ["print", "(", "banana", ".", "count", "(", "\"", "a", "\"", ")", ")"],
    ["a", "=", "5", "/n", "b", "=", "3", "/n", "print", "(", "a", "+", "b", ")"],
    ["def", "f", "(", "x", ")", ":", "/n", "return", "x", "*", "x"],
    ["import", "math", "/n", "area_circulo", "=", "math.pi", "*", "r", "**", "2"],
    ["str1", "=", "\"", "ejemplo", "de", "cadena", "\"", "/n", "print", "(", "str1", ")"],
    ["nombre", "=", "\"", "tetris", "\"", "/n", "print", "(", "nombre", "[", "0", "]", ")"],
    ["text", "=", "\"", "Cien", "años", "\"", "/n", "if", "\"", "años", "\"", "in", "text", ":", "print", "(", "\"", "yes", "\"", ")"],
    ["import", "random", "/n", "print", "(", "random", ".", "randint", "(", "0", ",", "10", ")", ")"],
    ["persona", "=", "{", "\"", "nombre", "\"", ":", "\"", "Carlos", "\"", ",", "\"", "edad", "\"", ":", "30", "}"],
    ["with", "open", "(", "archivo", ".", "txt", ",", "\"", "r", "\"", ")", "as", "f", "/n", "cont", "=", "f", ".", "read", "(", ")"]
]

class Piece:
    def __init__(self, text):
        self.text = text
        self.x = random.randint(0, COLUMNS - 1)
        self.y = 0

    def move(self, dx, dy, words):
        if self.valid_position(dx, dy, words):
            self.x += dx
            self.y += dy
            return True
        return False
    
    def drop(self, words):
        while self.move(0, 1, words):
            pass
        return False

    def valid_position(self, dx, dy, words):
        new_x = self.x + dx
        new_y = self.y + dy
        if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS or any(w[1] == new_x and w[2] == new_y for w in words):
            return False
        return True

def draw_grid(screen):
    for y in range(ROWS):
        for x in range(COLUMNS):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

def draw_piece(screen, piece, font):
    text_surface = font.render(piece.text, True, WHITE)
    text_rect = text_surface.get_rect(center=((piece.x * GRID_SIZE) + GRID_SIZE // 2, (piece.y * GRID_SIZE) + GRID_SIZE // 2))
    screen.blit(text_surface, text_rect)

def draw_words(screen, words, font):
    for word, x, y in words:
        text_surface = font.render(word, True, WHITE)
        text_rect = text_surface.get_rect(center=((x * GRID_SIZE) + GRID_SIZE // 2, (y * GRID_SIZE) + GRID_SIZE // 2))
        screen.blit(text_surface, text_rect)

def draw_level_complete(screen, level, font_medium, font_small):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180)) 
    screen.blit(overlay, (0, 0))

    message = "¡Avanzaste de nivel!"
    text_surface = font_medium.render(message, True, GREEN)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))
    screen.blit(text_surface, text_rect)

    code_message = "El código obtenido fue:"
    code_surface = font_small.render(code_message, True, WHITE)
    code_rect = code_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(code_surface, code_rect)

    code_string = level_to_string(LEVELS[level])
    code_lines = code_string.split('\n')
    y_offset = 40
    for line in code_lines:
        code_surface = font_small.render(line, True, GREEN)
        code_rect = code_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
        screen.blit(code_surface, code_rect)
        y_offset += 30

def draw_info(screen, score, lines_cleared, elapsed_time, level, errors, available_words, font):
    info_rect = pygame.Rect(GRID_WIDTH, 0, INFO_WIDTH, HEIGHT)
    pygame.draw.rect(screen, DARK_BG, info_rect)

    score_text = font.render(f"Puntaje: {score}", True, WHITE)
    lines_text = font.render(f"Lineas: {lines_cleared}", True, WHITE)
    time_text = font.render(f"Tiempo: {elapsed_time:.1f}s", True, WHITE)
    level_text = font.render(f"Nivel: {level + 1}", True, WHITE)

    error_color = RED if errors >= MAX_ERRORS else WHITE
    error_text = font.render(f"Errores: {errors}/{MAX_ERRORS}", True, error_color)
    
    screen.blit(score_text, (GRID_WIDTH + 30, 30))
    screen.blit(lines_text, (GRID_WIDTH + 30, 70))
    screen.blit(time_text, (GRID_WIDTH + 30, 110))
    screen.blit(level_text, (GRID_WIDTH + 30, 150))
    screen.blit(error_text, (GRID_WIDTH + 30, 190))

    title_text = font.render("Codigo a completar:", True, WHITE)
    screen.blit(title_text, (GRID_WIDTH + 40, 240))

    code_x = GRID_WIDTH + 30
    code_y = 280
    line_height = 30
    max_width = INFO_WIDTH - 60 
    current_width = 0
    first_line = True

    for i, word in enumerate(LEVELS[level]):
        word_text = font.render(word, True, GREEN)
        word_width = word_text.get_width() + 10 

        if current_width + word_width > max_width and not first_line:
            code_x = GRID_WIDTH + 30
            code_y += line_height
            current_width = 0

        screen.blit(word_text, (code_x, code_y))
        code_x += word_width
        current_width += word_width
        first_line = False

    available_title = font.render("Palabras disponibles:", True, WHITE)
    screen.blit(available_title, (GRID_WIDTH + 30, code_y + 60))

    word_x = GRID_WIDTH + 30
    word_y = code_y + 100
    
    for word in available_words:
        word_text = font.render(word, True, BLUE)
        word_width = word_text.get_width()
        screen.blit(word_text, (word_x, word_y))
        word_x += word_width + 10 

    controls_title = font.render("Controles:", True, WHITE)
    screen.blit(controls_title, (GRID_WIDTH + 30, word_y + 60))
    
    move_text = font.render("← → : Mover pieza", True, WHITE)
    down_text = font.render("↓ : Bajar pieza", True, WHITE)
    drop_text = font.render("Enter : Soltar pieza", True, WHITE)
    change_text = font.render("E : Cambiar palabra", True, WHITE)
    menu_text = font.render("ESC : Volver al menú", True, WHITE)
    
    screen.blit(move_text, (GRID_WIDTH + 30, word_y + 90))
    screen.blit(down_text, (GRID_WIDTH + 30, word_y + 120))
    screen.blit(drop_text, (GRID_WIDTH + 30, word_y + 150))
    screen.blit(change_text, (GRID_WIDTH + 30, word_y + 180))
    screen.blit(menu_text, (GRID_WIDTH + 30, word_y + 210))

def draw_message(screen, message, color, font, y_offset=0):
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50 + y_offset))
    screen.blit(text_surface, text_rect)

def validate_code(words, level):
    if not words:  
        return words, 0, False

    sorted_words = sorted(words, key=lambda w: (w[2], w[1]))

    rows = {}
    for word in sorted_words:
        y = word[2]
        if y not in rows:
            rows[y] = []
        rows[y].append(word)

    level_code = LEVELS[level]
    
    for y in sorted(rows.keys()):
        row_words = sorted(rows[y], key=lambda w: w[1])
        row_text = [w[0] for w in row_words]

        if len(row_text) == len(level_code):
            if row_text == level_code:
                return [w for w in words if w[2] != y], 1, False
            else:
                return [], 0, True
    
    return words, 0, False

def reset_level(level):
    available_words = LEVELS[level].copy()
    random.shuffle(available_words)
    falling_piece = Piece(available_words.pop(0))
    return [], available_words, falling_piece

def draw_main_menu(screen, font_large, font_medium, font_small):
    screen.fill(BLACK)
    
    title = font_large.render("Tetris Py", True, WHITE)
    subtitle = font_medium.render("Aprende Python mientras juegas", True, WHITE)
    start_text = font_medium.render("Presiona ESPACIO para comenzar", True, GREEN)
    
    controls_title = font_small.render("Controles:", True, WHITE)
    controls_move = font_small.render("← → : Mover pieza", True, WHITE)
    controls_down = font_small.render("↓ : Bajar pieza", True, WHITE)
    controls_drop = font_small.render("Enter : Soltar pieza", True, WHITE)
    controls_change = font_small.render("E : Cambiar palabra", True, WHITE)
    controls_menu = font_small.render("ESC : Volver al menú", True, WHITE)
    
    title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    subtitle_rect = subtitle.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
    
    controls_title_rect = controls_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 120))
    controls_move_rect = controls_move.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 160))
    controls_down_rect = controls_down.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 190))
    controls_drop_rect = controls_drop.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 220))
    controls_change_rect = controls_change.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 250))
    controls_menu_rect = controls_menu.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 280))
    
    screen.blit(title, title_rect)
    screen.blit(subtitle, subtitle_rect)
    screen.blit(start_text, start_rect)
    screen.blit(controls_title, controls_title_rect)
    screen.blit(controls_move, controls_move_rect)
    screen.blit(controls_down, controls_down_rect)
    screen.blit(controls_drop, controls_drop_rect)
    screen.blit(controls_change, controls_change_rect)
    screen.blit(controls_menu, controls_menu_rect)

def get_fall_speed(level):
    return max(BASE_FALL_SPEED - (level * SPEED_INCREASE_PER_LEVEL), 200)

def maingame():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris Py")
    clock = pygame.time.Clock()

    try:
        font = pygame.font.Font(FONT_PATH, 16)
        font_large = pygame.font.Font(FONT_PATH, 36)
        font_medium = pygame.font.Font(FONT_PATH, 24)
        font_small = pygame.font.Font(FONT_PATH, 16)
    except:
        font = pygame.font.SysFont("monospace", 16)
        font_large = pygame.font.SysFont("monospace", 36)
        font_medium = pygame.font.SysFont("monospace", 24)
        font_small = pygame.font.SysFont("monospace", 16)

    in_menu = True
    words = []
    level = 0
    words, available_words, falling_piece = reset_level(level)
    running = True
    fall_time = 0
    score = 0
    lines_cleared = 0
    errors = 0 
    start_time = pygame.time.get_ticks()
    game_over = False
    game_won = False
    showing_level_message = False
    level_message_start = 0

    while running:
        if in_menu:
            draw_main_menu(screen, font_large, font_medium, font_small)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        in_menu = False
                        level = 0
                        words, available_words, falling_piece = reset_level(level)
                        score = 0
                        lines_cleared = 0
                        errors = 0
                        start_time = pygame.time.get_ticks()
                        game_over = False
                        game_won = False
                        showing_level_message = False
        else:
            screen.fill(BLACK)
            if not game_over and not game_won:
                elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
            
            draw_grid(screen)
            if falling_piece:
                draw_piece(screen, falling_piece, font)
            draw_words(screen, words, font)
            draw_info(screen, score, lines_cleared, elapsed_time, level, errors, available_words, font)

            if showing_level_message:
                draw_level_complete(screen, level - 1, font_medium, font_small)
                if pygame.time.get_ticks() - level_message_start > LEVEL_MESSAGE_DURATION:
                    showing_level_message = False

            if game_over:
                overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 200))  
                screen.blit(overlay, (0, 0))
                
                draw_message(screen, "JUEGO TERMINADO!", RED, font_medium)
                
                error_text = font_small.render(f"Has cometido {errors} errores de {MAX_ERRORS} permitidos.", True, WHITE)
                score_text = font_small.render(f"Puntaje final: {score} | Tiempo: {elapsed_time:.1f}s", True, WHITE)
                restart_text = font_small.render("Presiona ESPACIO para reiniciar", True, GREEN)
                exit_text = font_small.render("Presiona ESC para volver al menú", True, WHITE)
                
                error_rect = error_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
                score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
                restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
                exit_rect = exit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 140))
                
                screen.blit(error_text, error_rect)
                screen.blit(score_text, score_rect)
                screen.blit(restart_text, restart_rect)
                screen.blit(exit_text, exit_rect)

                
            elif game_won:
                overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 200))
                screen.blit(overlay, (0, 0))
                
                draw_message(screen, "FELICIDADES!", GREEN, font_medium)
                
                win_text = font_small.render("HAS GANADO!", True, GREEN)
                score_text = font_small.render(f"Puntaje final: {score} | Tiempo: {elapsed_time:.1f}s", True, WHITE)
                restart_text = font_small.render("Presiona ESPACIO para reiniciar", True, GREEN)
                exit_text = font_small.render("Presiona ESC para volver al menú", True, WHITE)
                
                win_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
                score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
                restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
                exit_rect = exit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 140))
                
                screen.blit(win_text, win_rect)
                screen.blit(score_text, score_rect)
                screen.blit(restart_text, restart_rect)
                screen.blit(exit_text, exit_rect)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if game_over or game_won:
                        if event.key == pygame.K_SPACE:
                            level = 0
                            words, available_words, falling_piece = reset_level(level)
                            score = 0
                            lines_cleared = 0
                            errors = 0
                            start_time = pygame.time.get_ticks()
                            game_over = False
                            game_won = False
                            showing_level_message = False
                        elif event.key == pygame.K_ESCAPE:
                            in_menu = True
                    elif falling_piece:
                        if event.key == pygame.K_LEFT:
                            falling_piece.move(-1, 0, words)
                        elif event.key == pygame.K_RIGHT:
                            falling_piece.move(1, 0, words)
                        elif event.key == pygame.K_DOWN:
                            falling_piece.move(0, 1, words)
                        elif event.key == pygame.K_RETURN:
                            falling_piece.drop(words)
                            words.append((falling_piece.text, falling_piece.x, falling_piece.y))

                            words, cleared, has_error = validate_code(words, level)
                            if cleared > 0:
                                lines_cleared += cleared
                                score += cleared * 100
                                
                                if level < len(LEVELS) - 1:
                                    showing_level_message = True
                                    level_message_start = pygame.time.get_ticks()
                                    level += 1
                                    words, available_words, falling_piece = reset_level(level)
                                else:
                                    game_won = True
                                    falling_piece = None
                            else:
                                if has_error:
                                    errors += 1
                                    if errors >= MAX_ERRORS:
                                        game_over = True
                                        falling_piece = None
                                    else:
                                        words, available_words, falling_piece = reset_level(level)
                                else:
                                    if available_words:
                                        next_word = available_words.pop(0)
                                        falling_piece = Piece(next_word)
                                    else:
                                        falling_piece = None
                                        if words:
                                            errors += 1
                                            if errors >= MAX_ERRORS:
                                                game_over = True
                                            else:
                                                words, available_words, falling_piece = reset_level(level)
                        elif event.key == pygame.K_e:
                            if available_words:
                                current_word = falling_piece.text
                                next_word = available_words.pop(0)
                                available_words.append(current_word)
                                falling_piece.text = next_word
                        elif event.key == pygame.K_ESCAPE:
                            in_menu = True
                        elif event.key == pygame.K_F1:
                            running = False

            if not game_over and not game_won and falling_piece:
                fall_time += clock.get_time()
                current_fall_speed = get_fall_speed(level)
                if fall_time > current_fall_speed:
                    if not falling_piece.move(0, 1, words):
                        words.append((falling_piece.text, falling_piece.x, falling_piece.y))

                        words, cleared, has_error = validate_code(words, level)
                        if cleared > 0:
                            lines_cleared += cleared
                            score += cleared * 100
                            
                            if level < len(LEVELS) - 1:
                                showing_level_message = True
                                level_message_start = pygame.time.get_ticks()
                                level += 1
                                words, available_words, falling_piece = reset_level(level)
                            else:
                                game_won = True
                                falling_piece = None
                        else:
                            if has_error:
                                errors += 1
                                if errors >= MAX_ERRORS:
                                    game_over = True
                                    falling_piece = None
                                else:
                                    words, available_words, falling_piece = reset_level(level)
                            else:
                                if available_words:
                                    next_word = available_words.pop(0)
                                    falling_piece = Piece(next_word)
                                else:
                                    falling_piece = None
                                    if words:
                                        errors += 1
                                        if errors >= MAX_ERRORS:
                                            game_over = True
                                        else:
                                            words, available_words, falling_piece = reset_level(level)

                    fall_time = 0

        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
    return [score, lines_cleared, level, elapsed_time]

if __name__ == "__main__":
    print(maingame())