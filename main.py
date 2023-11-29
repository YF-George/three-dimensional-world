import pygame
import sys
import math

# 初始化pygame
pygame.init()

# 獲取用戶指定的窗口大小，如果沒有指定，則使用默認大小
width = int(sys.argv[1]) if len(sys.argv) > 1 else 800
height = int(sys.argv[2]) if len(sys.argv) > 2 else 600

# 創建窗口
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D 中空圖形")

# 定義顏色
white = (255, 255, 255)
red = (255, 0, 0)

# 初始化圓形的位置
circle_radius = 5
circle_x = width // 2
circle_y = height // 2

# 定義視野參數
view_length = 500  # 視野的長度
view_angle = 45  # 扇形的角度
view_color = (0, 255, 0)  # 綠色

# 定義矩形參數
rect_width, rect_height = 200, 150
rect_x = (width - rect_width) // 2
rect_y = (height - rect_height) // 2

# 在平面圖上繪製空心矩形、空心點和視野
def draw_2d_plane():
    screen.fill(white)  # 填充白色背景

    # 繪製空心矩形
    pygame.draw.rect(screen, red, (rect_x, rect_y, rect_width, rect_height), 1)

    # 繪製空心點
    pygame.draw.circle(screen, red, (circle_x, circle_y), circle_radius, 1)

    # 計算視野的結束點
    view_end_x = int(circle_x + view_length * math.cos(math.radians(view_angle / 2)))
    view_end_y = int(circle_y - view_length * math.sin(math.radians(view_angle / 2)))

    # 繪製扇形視野
    pygame.draw.polygon(screen, view_color, [(circle_x, circle_y), (view_end_x, view_end_y), (circle_x, circle_y)], 0)

    # 繪製矩形牆壁
    pygame.draw.rect(screen, red, (rect_x, rect_y, rect_width, rect_height), 0)

    # 在視野方向生成直線上的點，直到碰到矩形牆壁
    step_size = 1
    current_x, current_y = circle_x, circle_y
    while 0 <= current_x < width and 0 <= current_y < height:
        pygame.draw.circle(screen, red, (int(current_x), int(current_y)), 2)
        current_x += step_size * math.cos(math.radians(view_angle / 2))
        current_y -= step_size * math.sin(math.radians(view_angle / 2))

        # 檢測是否碰到矩形牆壁，如果碰到就停止生成點
        if rect_x <= current_x <= rect_x + rect_width and rect_y <= current_y <= rect_y + rect_height:
            break

    pygame.display.update()  # 手動更新屏幕

# 主循環
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 監聽按鍵事件，並更新圓形的位置
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                circle_x -= 10
            elif event.key == pygame.K_RIGHT:
                circle_x += 10
            elif event.key == pygame.K_UP:
                circle_y -= 10
            elif event.key == pygame.K_DOWN:
                circle_y += 10

    draw_2d_plane()
    clock.tick(60)  # 控制遊戲循環的速度，這裡設定為每秒最多60次
