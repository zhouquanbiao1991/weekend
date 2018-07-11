import QtQuick 2.9
import QtQuick.Controls 2.2

Page {
    width: 600
    height: 400
    property alias listView: listView

    title: qsTr("Page 1")

    Label {
        text: qsTr("This is Task List")
        anchors.verticalCenterOffset: -157
        anchors.horizontalCenterOffset: 0
        anchors.centerIn: parent
    }
    ListView{
        id: listView
        x: 68
        y: 74
        width: 465
        height: 283
        model: ListModel{
            id:taskMo
            ListElement{
                time: "1351"
                title:"451651"
                content:"1516"
            }
        }
        delegate: taskDelegate
    }
    Component{
        id: taskDelegate
        Item{
            id:wrapper
            width: parent
            height: 30
            MouseArea{
                anchors.fill: parent.left
                onClicked: wrapper.ListView.view.curIndex = index
            }
        }
    }
}
