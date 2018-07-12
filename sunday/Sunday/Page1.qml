import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.3

Page {
    width: 600
    height: 400
    property alias listView: listView

    title: qsTr("Page 1")

    Label {
        width: 85
        height: 14
        text: qsTr("Task List")
        textFormat: Text.PlainText
        fontSizeMode: Text.Fit
        horizontalAlignment: Text.AlignHCenter
        anchors.verticalCenterOffset: -183
        anchors.horizontalCenterOffset: 1
        anchors.centerIn: parent
    }
    Component{
        id: taskDelegate
        Item {
            id:wrapper
            width: parent.width
            height: 30
            MouseArea{
                anchors.fill: parent
                onClicked: wrapper.ListView.view.currentIndex = index
            }
            RowLayout{
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                spacing: 8
                Text {
                    text: title
                    color: wrapper.ListView.isCurrentItem?"red":"black"
                    font.pixelSize: wrapper.ListView.isCurrentItem?22:18
                    Layout.preferredWidth: 120
                }
                Text {
                    text: time
                    color: wrapper.ListView.isCurrentItem?"red":"black"
                    font.pixelSize: wrapper.ListView.isCurrentItem?22:18
                    Layout.preferredWidth: 120
                }
                Text {
                    text: content
                    color: wrapper.ListView.isCurrentItem?"red":"black"
                    font.pixelSize: wrapper.ListView.isCurrentItem?22:18
                    Layout.preferredWidth: 120
                }
            }
        }
    }
    Component{
        id: headerView
        Item {
            id:wrapper
            width: parent.width
            height: 30
            MouseArea{
                anchors.fill: parent
                onClicked: wrapper.ListView.view.currentIndex = index
            }
            RowLayout{
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                spacing: 8
                Text {
                    text: "title"
                    color: wrapper.ListView.isCurrentItem?"red":"black"
                    font.pixelSize: wrapper.ListView.isCurrentItem?22:18
                    Layout.preferredWidth: 120
                }
                Text {
                    text: "time"
                    color: wrapper.ListView.isCurrentItem?"red":"black"
                    font.pixelSize: wrapper.ListView.isCurrentItem?22:18
                    Layout.preferredWidth: 120
                }
                Text {
                    text: "content"
                    color: wrapper.ListView.isCurrentItem?"red":"black"
                    font.pixelSize: wrapper.ListView.isCurrentItem?22:18
                    Layout.preferredWidth: 120
                }
            }
        }
    }

    ListView{
        id: listView
        anchors.rightMargin: 0
        anchors.bottomMargin: 0
        anchors.leftMargin: 0
        anchors.topMargin: 38
        anchors.fill: parent
        delegate: taskDelegate
        header: headerView


        model: ListModel{
            id:taskModel
            ListElement{
                time: "1"
                title:"2"
                content:"3"
            }
            ListElement{
                time: "4"
                title:"5"
                content:"6"
            }
            ListElement{
                time: "7"
                title:"8"
                content:"9"
            }
        }

        focus: true
        highlight: Rectangle{
            color: "lightblue"
        }
    }
}
