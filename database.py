

class Player:
  def __init__(self, userID, name, gameName):
    self.id = userID
    self.name = name
    self.gameName = gameName
    self.gameStatus = {}

  def updateName(self, name):
    self.name = name

  def updateGameName(self, gameName):
    self.gameName = gameName

  def parseStatus(statusStr):
    status = {}
    log = ""
    while (len(statusStr)):
      # 获取名称
      typeIdx = 0
      while not statusStr[typeIdx].isdigit():
        typeIdx += 1
      # 获取数字
      valueIdx = typeIdx
      while statusStr[valueIdx].isdigit():
        valueIdx += 1
      # 录入
      # TODO: Exception 需要检查录入合法性
      # TODO: 检查是否已经存在
      status[statusStr[0:typeIdx]] = statusStr[typeIdx:valueIdx]
    return status, log

  def createGameStatus(self, statusStr):
    self.gameStatus, _ = parseStatus(statusStr)
    
    

class NameDB:
  def __init__(self):
    return

  # Update the user list / group / 
  def update(self):
    