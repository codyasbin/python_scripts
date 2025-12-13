import time
import math

def amazing_animation():
    """Amazing animated star burst with color gradients"""
    
    print("\n" + "="*60)
    print("✨ AMAZING PYTHON ANIMATION ✨".center(60))
    print("="*60 + "\n")
    
    # Spinning loading animation
    spinners = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    print("Loading amazing content")
    for i in range(20):
        print(f'\r{spinners[i % len(spinners)]} ', end='', flush=True)
        time.sleep(0.1)
    print("\n✓ Ready!\n")
    
    # Animated pyramid
    print("Dynamic Pyramid:")
    for i in range(1, 8):
        spaces = " " * (7 - i)
        bars = "█" * (i * 2 - 1)
        print(spaces + bars)
        time.sleep(0.15)
    
    print("\n" + "-"*60)
    
    # Animated circle/spiral
    print("\nSpin Animation:")
    size = 5
    for frame in range(16):
        angle = (frame / 16) * 2 * math.pi
        x = int(size * math.cos(angle))
        y = int(size * math.sin(angle))
        print(f'\r{"." * (size + x)}●', end='', flush=True)
        time.sleep(0.1)
    print("\n")
    
    # Rainbow pattern
    print("Rainbow Wave Pattern:")
    colors = ['🔴', '🟠', '🟡', '🟢', '🔵', '🟣']
    for row in range(6):
        for col in range(10):
            print(colors[(row + col) % len(colors)], end=' ')
        print()
        time.sleep(0.2)
    
    print("\n" + "-"*60)
    
    # ASCII art fireworks
    print("\n🎆 FIREWORKS DISPLAY 🎆\n")
    fireworks = [
        "    *     ",
        "   * *    ",
        "  *   *   ",
        " *     *  ",
        "*       * "
    ]
    
    for _ in range(3):
        for frame in fireworks:
            print(frame)
            time.sleep(0.1)
        print()
        time.sleep(0.3)
    
    # Expanding box animation
    print("\n" + "-"*60)
    print("\nExpanding Box:")
    for size in range(1, 6):
        for i in range(size):
            if i == 0 or i == size - 1:
                print("█" * (size * 2))
            else:
                print("█" + " " * (size * 2 - 2) + "█")
        time.sleep(0.3)
        print()
    
    # Final celebration
    print("\n" + "="*60)
    print("✨ YOU HAVE BEEN AMAZED! ✨".center(60))
    print("="*60)
    
    # Bouncing text
    print("\nBouncing text:")
    for bounce in range(3):
        for space in range(20):
            print(" " * space + "⭐ AWESOME! ⭐", flush=True)
            time.sleep(0.05)
        for space in range(20, 0, -1):
            print(" " * space + "⭐ AWESOME! ⭐", flush=True)
            time.sleep(0.05)
    
    print("\n" + "="*60)
    print("Thanks for watching! 🎉".center(60))
    print("="*60 + "\n")

if __name__ == "__main__":
    amazing_animation()
