import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.3

Page {
    width: 600
    height: 400
    //property alias listView: listView

    title: qsTr("Page 1")
    //model
    Component{
        id: taskModel
        ListModel{
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
    }
    //head
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
    //foot
    Component{
        id: footView
        Text{
            width: 60
            height: 30
            text: "abc"
        }
    }
    //delegate
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

    ListView{
        id: listView
        anchors.rightMargin: 0
        anchors.bottomMargin: 0
        anchors.leftMargin: 0
        anchors.topMargin: 0
        anchors.fill: parent

        delegate: taskDelegate
        model: taskModel.createObject(listView)
        header: headerView
        footer: footView

        focus: true
        highlight: Rectangle{
            color: "lightblue"
        }
    }
}
