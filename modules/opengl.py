from OpenGL.GL import glGetString, GL_VERSION
import pygame

# Inicializa uma janela para acessar a OpenGL
pygame.init()
pygame.display.set_mode((100, 100), pygame.OPENGL | pygame.DOUBLEBUF)

# Obtém a versão do OpenGL
opengl_version = glGetString(GL_VERSION).decode()

print(f"Versão do OpenGL: {opengl_version}")

pygame.quit()
