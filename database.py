import discord

class Player:
  def __init__(self, playerName):
    self.playerName = playerName
    self.playerStatus = {}

  def updateGameName(self, playerName):
    self.playerName = playerName

  def parseStatus(self, playerStatus):
    status = {}
    while (len(playerStatus)):
      # 获取名称
      typeIdx = 0
      while not playerStatus[typeIdx].isdigit():
        typeIdx += 1
      # 获取数字
      valueIdx = typeIdx
      while playerStatus[valueIdx].isdigit():
        valueIdx += 1
      # 录入
      # TODO: Exception 需要检查录入合法性
      # TODO: 检查是否已经存在
      status[playerStatus[0:typeIdx]] = playerStatus[typeIdx:valueIdx]
      # 删除已录入的部分
      playerStatus = playerStatus[valueIdx:]
    return status, len(status.keys())

  def createGameStatus(self, statusStr):
    self.playerStatus, amount = self.parseStatus(statusStr[4:])
    return amount


USER = "USER"
PLAYER = "PLAYER"
KP = "KP"

class Member:
  def __init__(self, type, discordMsg):
    self.type = type
    self.player = None
    if type == PLAYER:
      self.player = Player(discordMsg.author.nick, discordMsg)

  def createGameStatus(self, statusStr):
    return self.player.createGameStatus(statusStr)



class MemberDataBase:
  def __init__(self):
    self.memberDB = {}

  def getMember(self, discordMsg):
    if discordMsg.author.id in self.memberDB.keys():
      return self.memberDB[discordMsg.author.id]
    return None

  def addPlayer(self, discordMsg):
    userID = discordMsg.author.id
    self.memberDB[userID] = Member(PLAYER, discordMsg)
    return self.memberDB[userID].createGameStatus(discordMsg.content)

  def checkStatus(self, discordMsg):
    if discordMsg.author.id in self.memberDB.keys():
      return checkStatus(self, discordMsg)
    
    