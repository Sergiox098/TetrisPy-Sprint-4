import pygame
import random

WIDTH, HEIGHT = 1000, 700  
GRID_SIZE = 30
GRID_WIDTH = 600  
INFO_WIDTH = WIDTH - GRID_WIDTH
COLUMNS = GRID_WIDTH // GRID_SIZE
ROWS = HEIGHT // GRID_SIZE
MAX_ERRORS = 3  

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (255, 50, 50)
GREEN = (50, 255, 50)

FONT_PATH = "PressStart2P-Regular.ttf"

LEVELS = [
    ["print", "(", "\"", "Hola", "mundo", "\"", ")"],
    ["variable", "=", "print", "(", "\"", "Hola", "mundo", "\"", ")"],
    ["edad", "=", "int", "(", "input", "(", "\"", "años", "\"", ")", ")"]
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

def draw_piece(screen, piece):
    font = pygame.font.Font(FONT_PATH, 16)
    text_surface = font.render(piece.text, True, WHITE)
    text_rect = text_surface.get_rect(center=((piece.x * GRID_SIZE) + GRID_SIZE // 2, (piece.y * GRID_SIZE) + GRID_SIZE // 2))
    screen.blit(text_surface, text_rect)

def draw_words(screen, words):
    font = pygame.font.Font(FONT_PATH, 16)
    for word, x, y in words:
        text_surface = font.render(word, True, WHITE)
        text_rect = text_surface.get_rect(center=((x * GRID_SIZE) + GRID_SIZE // 2, (y * GRID_SIZE) + GRID_SIZE // 2))
        screen.blit(text_surface, text_rect)

def draw_info(screen, score, lines_cleared, elapsed_time, level, errors):
    font = pygame.font.Font(FONT_PATH, 16)
    
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

def draw_message(screen, message, color=RED):
    font = pygame.font.Font(FONT_PATH, 24)
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
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

    has_error = False
    level_code = LEVELS[level]
    
    for y in sorted(rows.keys()):
        row_words = sorted(rows[y], key=lambda w: w[1])
        row_text = [w[0] for w in row_words]

        if len(row_text) == len(level_code):
            if row_text == level_code:
                return [w for w in words if w[2] != y], 1, False
            else:
                has_error = True
                return [w for w in words if w[2] != y], 0, has_error
    
    return words, 0, has_error

def reset_level(level):
    available_words = LEVELS[level].copy()
    random.shuffle(available_words)
    falling_piece = Piece(available_words.pop(0))
    return [], available_words, falling_piece

def maingame():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris Py")
    clock = pygame.time.Clock()
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

    while running:
        screen.fill(BLACK)
        if not game_over and not game_won:
            elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        
        draw_grid(screen)
        if falling_piece:
            draw_piece(screen, falling_piece)
        draw_words(screen, words)
        draw_info(screen, score, lines_cleared, elapsed_time, level, errors)

        font = pygame.font.Font(FONT_PATH, 16)
        title_text = font.render("Codigo a completar:", True, WHITE)
        screen.blit(title_text, (GRID_WIDTH + 30, 240))

        for i, word in enumerate(LEVELS[level]):
            word_text = font.render(word, True, WHITE)
            screen.blit(word_text, (GRID_WIDTH + 30, 280 + i * 30))

        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 200))  
            screen.blit(overlay, (0, 0))
            
            draw_message(screen, "JUEGO TERMINADO!")
            
            small_font = pygame.font.Font(FONT_PATH, 16)
            error_text = small_font.render(f"Has cometido {errors} errores de {MAX_ERRORS} permitidos.", True, WHITE)
            score_text = small_font.render(f"Puntaje final: {score} | Tiempo: {elapsed_time:.1f}s", True, WHITE)
            restart_text = small_font.render("Presiona ESPACIO para reiniciar", True, WHITE)
            
            error_rect = error_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
            score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
            restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
            
            screen.blit(error_text, error_rect)
            screen.blit(score_text, score_rect)
            screen.blit(restart_text, restart_rect)
            
        elif game_won:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 200))
            screen.blit(overlay, (0, 0))
            
            draw_message(screen, "FELICIDADES!", GREEN)
            
            small_font = pygame.font.Font(FONT_PATH, 16)
            win_text = small_font.render("HAS GANADO!", True, GREEN)
            score_text = small_font.render(f"Puntaje final: {score} | Tiempo: {elapsed_time:.1f}s", True, WHITE)
            restart_text = small_font.render("Presiona ESPACIO para reiniciar", True, WHITE)
            
            win_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
            score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
            restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
            
            screen.blit(win_text, win_rect)
            screen.blit(score_text, score_rect)
            screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()

        fall_time += clock.get_time()
        if fall_time > 1000 and not game_over and not game_won and falling_piece:
            if not falling_piece.move(0, 1, words):
                words.append((falling_piece.text, falling_piece.x, falling_piece.y))

                words, cleared, has_error = validate_code(words, level)
                if cleared > 0:
                    lines_cleared += cleared
                    score += cleared * 100
                    
                    if level < len(LEVELS) - 1:
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
                            if not available_words:
                                _, available_words, _ = reset_level(level)
                            
                            next_word = available_words.pop(0)
                            falling_piece = Piece(next_word)
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
                                    _, available_words, _ = reset_level(level)
                                    next_word = available_words.pop(0)
                                    falling_piece = Piece(next_word)

            fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not game_over and not game_won:
                    if falling_piece:
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
                                        if not available_words:
                                            _, available_words, _ = reset_level(level)
                                        
                                        next_word = available_words.pop(0)
                                        falling_piece = Piece(next_word)
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
                                                _, available_words, _ = reset_level(level)
                                                next_word = available_words.pop(0)
                                                falling_piece = Piece(next_word)
                elif event.key == pygame.K_SPACE:
                    if game_over or game_won:
                        level = 0
                        words, available_words, falling_piece = reset_level(level)
                        score = 0
                        lines_cleared = 0
                        errors = 0
                        start_time = pygame.time.get_ticks()
                        game_over = False
                        game_won = False

        clock.tick(30)
    
    pygame.quit()