# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.5 on Sun May 24 20:12:57 2015

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
BUTTON_UP = 1000
BUTTON_DOWN = 1001
BUTTON_LEFT = 1002
BUTTON_RIGHT = 1003
BUTTON_SPEED = 1004
DIALOG_SIZE = (90, 90)


# end wxGlade


class GuideCtrlDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: GuideCtrlDialog.__init__
        kwds["style"] = wx.SYSTEM_MENU
        wx.Dialog.__init__(self, *args, **kwds)
        self.buttonUp = wx.ToggleButton(self, BUTTON_UP, "^")
        self.buttonLeft = wx.ToggleButton(self, BUTTON_LEFT, "<")
        self.buttonSpeed = wx.ToggleButton(self, BUTTON_SPEED, "Hi")
        self.buttonRight = wx.ToggleButton(self, BUTTON_RIGHT, ">")
        self.buttonDown = wx.ToggleButton(self, BUTTON_DOWN, "v")
        self.buttonClose = wx.BitmapButton(self, -1, wx.Bitmap("check.png", wx.BITMAP_TYPE_ANY))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: GuideCtrlDialog.__set_properties
        self.SetSize((90, 90))
        self.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.buttonUp.SetMinSize((30, 30))
        self.buttonUp.SetBackgroundColour(wx.Colour(64, 64, 64))
        self.buttonUp.SetForegroundColour(wx.Colour(255, 255, 255))
        self.buttonLeft.SetMinSize((30, 30))
        self.buttonLeft.SetBackgroundColour(wx.Colour(64, 64, 64))
        self.buttonLeft.SetForegroundColour(wx.Colour(255, 255, 255))
        self.buttonSpeed.SetMinSize((30, 30))
        self.buttonSpeed.SetBackgroundColour(wx.Colour(64, 64, 64))
        self.buttonSpeed.SetForegroundColour(wx.Colour(255, 255, 255))
        self.buttonRight.SetMinSize((30, 30))
        self.buttonRight.SetBackgroundColour(wx.Colour(64, 64, 64))
        self.buttonRight.SetForegroundColour(wx.Colour(255, 255, 255))
        self.buttonDown.SetMinSize((30, 30))
        self.buttonDown.SetBackgroundColour(wx.Colour(64, 64, 64))
        self.buttonDown.SetForegroundColour(wx.Colour(255, 255, 255))
        self.buttonClose.SetMinSize((28, 28))
        self.buttonClose.SetBackgroundColour(wx.Colour(64, 64, 64))
        self.buttonClose.SetForegroundColour(wx.Colour(255, 255, 255))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: GuideCtrlDialog.__do_layout
        grid_sizer_1 = wx.GridSizer(3, 3, 0, 0)
        grid_sizer_1.Add((30, 30), 0, 0, 0)
        grid_sizer_1.Add(self.buttonUp, 0, 0, 0)
        grid_sizer_1.Add((30, 30), 0, 0, 0)
        grid_sizer_1.Add(self.buttonLeft, 0, 0, 0)
        grid_sizer_1.Add(self.buttonSpeed, 0, 0, 0)
        grid_sizer_1.Add(self.buttonRight, 0, 0, 0)
        grid_sizer_1.Add((30, 30), 0, 0, 0)
        grid_sizer_1.Add(self.buttonDown, 0, 0, 0)
        grid_sizer_1.Add(self.buttonClose, 0, 0, 0)
        self.SetSizer(grid_sizer_1)
        self.Layout()
        # end wxGlade

# end of class GuideCtrlDialog