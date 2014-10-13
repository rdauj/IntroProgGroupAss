pic1 = makePicture(pickAFile())
pic2 = makePicture(pickAFile())
pic3 = makePicture(pickAFile())

canvas = makeEmptyPicture(2696,1037)

def master():
  #pic1 controls
  jack = scaleDown(pic1)  
  ##paste on canvas
  #pic2 controls
  queen = scaleDown(pic2)
  #pic3 controls
  king = scaleDown(pic3)
  #misc
  detectEdges(jack)
  halver(queen,king)
  halver ( jack, queen)
  
def cropper(pic, target, startX,startY):
  width 
  
  
  
def halver(pic2,pic1):
  width = getWidth(pic2)
  height = getHeight(pic2)
  for x in range(0,width):
    for y in range(0,height):
      originalPixel = getPixel(pic2,x/2,y)
      originalColor = getColor(originalPixel)
      targetPixel = getPixel(pic1,x/2,y)
      setColor(targetPixel,originalColor)
  repaint(pic1)
  
  
def scaleDown(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  canvas = makeEmptyPicture(337,520)
  for x in range(0,width,2):
    for y in range(0,height,2):
      originalPx = getPixel(pic,x,y)
      originalColour = getColor(originalPx)
      target = getPixel(canvas,x/2,y/2)
      setColor(target,originalColour)
  #repaint(canvas)
  return canvas

def detectEdges(pic):
  width=getWidth(pic)
  height=getHeight(pic)
  newPic=makeEmptyPicture(width,height)
  for pixel in getPixels(pic):
    x= getX(pixel)
    y= getY(pixel)
    if (x<(width-1)) and (y<(height-1)):
      pixelRight = getPixel(pic,x+1,y)
      pixelDown = getPixel(pic,x,y+1)
      here = (getRed(pixel)+getGreen(pixel)+getBlue(pixel))/3
      right =(getRed(pixelRight)+getGreen(pixelRight)+getBlue(pixelRight))
      down = (getRed(pixelDown)+getGreen(pixelDown)+getBlue(pixelDown))/3
      if abs(here-down)>10 and abs(here-right)>10:
        pixNew=getPixel(newPic,x,y)
        setColor(pixNew,black)
        if abs(here-down)<=10 and abs(here-right)<=10:
          pixNew=getPixel(newPic,x,y)
          setColor(pixNew,white)
      
  repaint (newPic)
