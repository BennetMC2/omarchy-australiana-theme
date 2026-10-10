import QtQuick
import Quickshell
import Quickshell.Io
import qs.Commons

// Decorative only: no input handlers, authentication state or focus changes.
Item {
  id: root
  property string themeName: ""
  visible: themeName === "australiana"
  FileView {
    path: Quickshell.env("HOME") + "/.local/state/omarchy/current/theme.name"
    watchChanges: true
    onFileChanged: reload()
    onLoaded: root.themeName = text().trim()
  }
  Column {
    anchors.horizontalCenter: parent.horizontalCenter
    y: Math.max(16, parent.height / 2 - height - 65)
    spacing: 12
    Image {
      anchors.horizontalCenter: parent.horizontalCenter
      width: 58
      height: 58
      source: "australiana-roo.svg"
      fillMode: Image.PreserveAspectFit
    }
    Text {
      anchors.horizontalCenter: parent.horizontalCenter
      text: "Gone walkabout"
      color: Color.foreground
      font.family: Style.font.family
      font.pixelSize: 30
      font.bold: true
      style: Text.Outline
      styleColor: Color.background
    }
    Text {
      anchors.horizontalCenter: parent.horizontalCenter
      text: "Back in a tick"
      color: Color.foreground
      font.family: Style.font.family
      font.pixelSize: 16
      style: Text.Outline
      styleColor: Color.background
    }
  }
}
