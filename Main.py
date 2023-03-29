#pip install sketchpy


from sketchpy import canvas
image = canvas.sketch_from_image('Your_IMAGE.JPEG') #Só testei em imagens com o formato jpeg
image.draw(threshold=145) #min 90, max 190 for best results






