
"use strict";

let WaypointSetCurrent = require('./WaypointSetCurrent.js')
let FileMakeDir = require('./FileMakeDir.js')
let FileRead = require('./FileRead.js')
let FileRemove = require('./FileRemove.js')
let FileRemoveDir = require('./FileRemoveDir.js')
let StreamRate = require('./StreamRate.js')
let FileList = require('./FileList.js')
let CommandTriggerControl = require('./CommandTriggerControl.js')
let WaypointClear = require('./WaypointClear.js')
let SetMavFrame = require('./SetMavFrame.js')
let FileOpen = require('./FileOpen.js')
let FileTruncate = require('./FileTruncate.js')
let CommandTOL = require('./CommandTOL.js')
let ParamPush = require('./ParamPush.js')
let CommandHome = require('./CommandHome.js')
let ParamPull = require('./ParamPull.js')
let CommandBool = require('./CommandBool.js')
let ParamGet = require('./ParamGet.js')
let ParamSet = require('./ParamSet.js')
let FileWrite = require('./FileWrite.js')
let CommandLong = require('./CommandLong.js')
let CommandInt = require('./CommandInt.js')
let FileClose = require('./FileClose.js')
let FileRename = require('./FileRename.js')
let SetMode = require('./SetMode.js')
let WaypointPull = require('./WaypointPull.js')
let WaypointPush = require('./WaypointPush.js')
let FileChecksum = require('./FileChecksum.js')

module.exports = {
  WaypointSetCurrent: WaypointSetCurrent,
  FileMakeDir: FileMakeDir,
  FileRead: FileRead,
  FileRemove: FileRemove,
  FileRemoveDir: FileRemoveDir,
  StreamRate: StreamRate,
  FileList: FileList,
  CommandTriggerControl: CommandTriggerControl,
  WaypointClear: WaypointClear,
  SetMavFrame: SetMavFrame,
  FileOpen: FileOpen,
  FileTruncate: FileTruncate,
  CommandTOL: CommandTOL,
  ParamPush: ParamPush,
  CommandHome: CommandHome,
  ParamPull: ParamPull,
  CommandBool: CommandBool,
  ParamGet: ParamGet,
  ParamSet: ParamSet,
  FileWrite: FileWrite,
  CommandLong: CommandLong,
  CommandInt: CommandInt,
  FileClose: FileClose,
  FileRename: FileRename,
  SetMode: SetMode,
  WaypointPull: WaypointPull,
  WaypointPush: WaypointPush,
  FileChecksum: FileChecksum,
};
