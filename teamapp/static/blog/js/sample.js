function confirmFunction1() {
    if( Window.confirm()("削除して大丈夫ですか？") ) {
        location.href="";
    }
    else {
        alert("移動をやめました。");
    }
}