import QtQuick 2.15
import QtQuick.Controls 2.15

Button {
    id: control
    text: "Button"

    contentItem: Text {
        text: control.text
        font.pixelSize: 14
        color: "#cdd6f4"
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }

    background: Rectangle {
        implicitWidth: 120
        implicitHeight: 36
        color: control.down ? "#74c7ec" : (control.hovered ? "#89b4fa" : "#313244")
        radius: 6
    }
}
