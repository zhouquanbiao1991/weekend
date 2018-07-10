import QtQuick 2.9
import QtQuick.Controls 2.2

Page {
    width: 600
    height: 400

    title: qsTr("Page 1")

    Label {
        text: qsTr("You are on Page 1.")
        anchors.centerIn: parent
    }
    Rectangle{
        width: 360
        height: 300
        TableView {
            id: taskTable
            anchors.fill: parent

        }
    }


}