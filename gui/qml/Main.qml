import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "components"

ApplicationWindow {
    id: rootWindow
    width: 900
    height: 600
    visible: true
    title: "Desktop App Template - PySide6 GUI"
    color: "#1e1e2e"

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 20

        Text {
            text: "Desktop App Template"
            font.pixelSize: 24
            font.bold: true
            color: "#cdd6f4"
            Layout.alignment: Qt.AlignHCenter
        }

        Text {
            text: "PySide6 Qt GUI + C++ Resource Engine + Python Deep Learning Middleware"
            font.pixelSize: 14
            color: "#a6adc8"
            Layout.alignment: Qt.AlignHCenter
        }

        AppButton {
            text: "Click Me"
            Layout.alignment: Qt.AlignHCenter
            onClicked: {
                console.log("Button clicked in QML!")
            }
        }
    }
}
