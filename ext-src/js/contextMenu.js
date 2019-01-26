var contextList = ["all"]

for(i=0 ;i<contextList.length;i++) {
    chrome.contextMenus.create({
        "id": contextList[i],
        "title": "Get_url",
        "contexts": [contextList[i]],

    });
}
chrome.contextMenus.onClicked.addListener(onClickHandler);

function onClickHandler(selectedText) {
chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
   function(tabs){
      alert(tabs[0].url);
   }
);
}