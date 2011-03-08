import Qt 4.7

Item {
    id: root
    width: 800
    height: 600

    signal scriptSelected(int plugin, int script)

    Component {
        id: selectedRow
        Rectangle {
            color: "gray"
            opacity: 0.4
        }
    }

    ListView {
        id: moduleList
        anchors {
            left: parent.left
            top: parent.top
            bottom: parent.bottom
        }
        highlight: selectedRow
        width: parent.width / 3
        model: plugins
        delegate: Component {
            Text {
                height: 30
                text: modelData.name
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        moduleList.currentIndex = index;
                        scriptList.model = modelData.scripts;
                    }
                }
            }
        }
    }

    ListView {
        id: scriptList
        anchors {
            left: moduleList.right
            top: parent.top
            bottom: parent.bottom
        }
        highlight: selectedRow
        width: parent.width / 3
        delegate: Component {
            Text {
                height: 30
                text: modelData.name
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        scriptList.currentIndex = index;
                    }
                }
            }
        }
    }

    Text {
        anchors {
            top: parent.top
            bottom: selectButton.top
            right: parent.right
            left: scriptList.right
        }
    }

    Rectangle {
        id: selectButton
        color: "gray"
        anchors {
            right: parent.right
            bottom: parent.bottom
            left: scriptList.right
        }
        height: 50
        radius: 15
        MouseArea {
            anchors.fill: parent
            onClicked: root.scriptSelected(
                moduleList.currentIndex, scriptList.currentIndex);
        }
    }
    onScriptSelected: {
        console.log(plugin + " & " + script)
    }
}