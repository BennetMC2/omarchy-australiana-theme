import QtQuick
import Quickshell
import Quickshell.Io
import qs.Commons
import qs.Ui

BarWidget {
  id: root
  moduleName: "australiana.roo"
  property string activeTheme: ""
  property bool muted: false
  readonly property string home: Quickshell.env("HOME")
  readonly property string control: home + "/.config/omarchy/themes/australiana/extras/australiana.py"
  visible: activeTheme === "australiana"
  implicitWidth: visible ? (vertical ? barSize : 34) : 0
  implicitHeight: visible ? barSize : 0

  FileView {
    path: root.home + "/.local/state/omarchy/current/theme.name"
    watchChanges: true
    onFileChanged: reload()
    onLoaded: root.activeTheme = text().trim()
  }
  FileView {
    path: root.home + "/.config/omarchy/australiana.json"
    watchChanges: true
    onFileChanged: reload()
    onLoaded: {
      try { root.muted = JSON.parse(text()).muted === true }
      catch (error) { root.muted = false }
    }
  }
  WidgetButton {
    anchors.fill: parent
    bar: root.bar
    hasVisualContent: true
    labelVisible: false
    tooltipText: "Australiana · Wallpapers\nRight-click: " + (root.muted ? "unmute" : "mute") + " kookaburra"
    onPressed: button => {
      if (button === Qt.RightButton)
        Quickshell.execDetached(["python3", root.control, "mute-toggle"])
      else if (button === Qt.LeftButton) {
        hop.restart()
        Quickshell.execDetached(["omarchy", "theme", "bg-switcher"])
      }
    }
    Image {
      id: roo
      width: 23
      height: Math.min(21, root.barSize - 4)
      x: (parent.width - width) / 2
      y: (parent.height - height) / 2
      source: "roo.svg"
      fillMode: Image.PreserveAspectFit
      opacity: root.muted ? 0.65 : 1
      transform: Translate { id: jump; y: 0 }
    }
  }
  SequentialAnimation {
    id: hop
    NumberAnimation { target: jump; property: "y"; to: -3; duration: 180; easing.type: Easing.OutQuad }
    NumberAnimation { target: jump; property: "y"; to: 0; duration: 220; easing.type: Easing.InQuad }
  }
  Timer {
    interval: 150000
    running: root.visible && root.setting("animate", true)
    repeat: true
    onTriggered: { hop.restart(); interval = 120000 + Math.floor(Math.random() * 180000) }
  }
  onVisibleChanged: if (!visible) { hop.stop(); jump.y = 0 }
}
