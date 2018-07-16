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
            id:taskDelegateItem
            width: parent.width
            height: 30
            MouseArea{
                anchors.fill: parent
                onClicked: taskDelegateItem.ListView.view.currentIndex = index
            }
            RowLayout{
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                spacing: 8
                Text {
                    text: "title"
                    color: taskDelegateItem.ListView.isCurrentItem?"red":"black"
                    font.pixelSize: taskDelegateItem.ListView.isCurrentItem?22:18
                    Layout.preferredWidth: 120
                }
                Text {
                    text: "time"
                    color: taskDelegateItem.ListView.isCurrentItem?"red":"black"
                    font.pixelSize: taskDelegateItem.ListView.isCurrentItem?22:18
                    Layout.preferredWidth: 120
                }
                Text {
                    text: "content"
                    color: taskDelegateItem.ListView.isCurrentItem?"red":"black"
                    font.pixelSize: taskDelegateItem.ListView.isCurrentItem?22:18
                    Layout.preferredWidth: 120
                }
            }
        }
    }
    //foot
    Component{
        id: footView
        Item{
            signal del();
            id: footerRootItem
            width: parent.width
            height: 30
            /*            Text{
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
            }*/
            RowLayout{
                height: 30
                width: parent.width
                Button {
                    id:addBtn
                    anchors.left: parent.left
                    anchors.verticalCenter: parent.verticalCenter
                    text: "add"
                    onClicked: {}
                }
                Button {
                    id:modifyBtn
                    anchors.left: addBtn.right
                    anchors.verticalCenter: parent.verticalCenter
                    text: "change"
                    onClicked: {}
                }
                Button {
                    id:delBtn
                    anchors.left: modifyBtn.right
                    anchors.verticalCenter: parent.verticalCenter
                    text: "delete"
                    onClicked: footerRootItem.del();
                }
            }
        }
    }
    //delegate
    Component{
        id: taskDelegate
        Item {
            id:taskDelegateItem
            width: parent.width
            height: 30
            MouseArea{
                anchors.fill: parent
                onClicked: taskDelegateItem.ListView.view.currentIndex = index
            }
            RowLayout{
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                spacing: 8
                Text {
                    text: title
                    color: taskDelegateItem.ListView.isCurrentItem?"red":"black"
                    font.pixelSize: taskDelegateItem.ListView.isCurrentItem?22:18
                    Layout.preferredWidth: 120
                }
                Text {
                    text: time
                    color: taskDelegateItem.ListView.isCurrentItem?"red":"black"
                    font.pixelSize: taskDelegateItem.ListView.isCurrentItem?22:18
                    Layout.preferredWidth: 120
                }
                Text {
                    text: content
                    color: taskDelegateItem.ListView.isCurrentItem?"red":"black"
                    font.pixelSize: taskDelegateItem.ListView.isCurrentItem?22:18
                    Layout.preferredWidth: 120
                }
            }
        }
    }

    ListView{
        id: listView
        anchors.fill: parent
        delegate: taskDelegate
        model: taskModel.createObject(listView)
        header: headerView
        footer: footView

        focus: true
        highlight: Rectangle{
            color: "lightblue"
        }

        onCurrentIndexChanged: {

        }

        function deleteItem(){
            model.remove(listView.currentIndex);
        }

        Component.onCompleted: {
            listView.footerItem.del.connect(listView.deleteItem);
        }
    }

    Rectangle{
        anchors.bottomMargin: 30
        anchors.left:parent.left
        anchors.bottom:parent.bottom
        width: parent.width

        GridLayout{
            anchors.left:parent.left
            anchors.bottom:parent.bottom
            width: parent.width
            height: 60
            rows:3
            rowSpacing: 3
            columns: 3
            columnSpacing: 3

            Text {
                id:time_text
                text: "Time:"
            }
            TextInput {
                id:time_input
                Layout.columnSpan: 2
            }

            Text {
                id:title_text
                text: "title:"
            }
            TextInput {
                id:title_input
                Layout.columnSpan: 2
                Layout.fillWidth: true
            }

            Text {
                id:content_text
                text: "content:"
            }
            TextInput {
                id:content_input
                Layout.columnSpan: 2

            }
            Button {
                id:add
                text: "add"
                Layout.fillWidth: true
                onClicked: {}
            }

            Button {
                id:modify
                text: "change"
                Layout.fillWidth: true
                onClicked: {}
            }
            Button {
                id:deleteBtn
                text: "delete"
                Layout.fillWidth: true
                onClicked: footerRootItem.del();
            }

        }
    }
}
