// Wait till the browser is ready to render the game (avoids glitches)
window.requestAnimationFrame(function () {
  new GameManager(4, KeyboardInputManager, HTMLActuator, LocalScoreManager);
});


    var imageList = [
        "https://www.oispakalussa.tk/img/2.png",
        "https://www.oispakalussa.tk/img/4.png",
        "https://www.oispakalussa.tk/img/8.png",
        "http://www.oispakaljaa.com/img/16.png",
        "http://www.oispakaljaa.com/img/32.png",
        "http://www.oispakaljaa.com/img/64.png",
        "http://www.oispakaljaa.com/img/128.png",
        "http://www.oispakaljaa.com/img/256.png",
        "http://www.oispakaljaa.com/img/512.png",
        "http://www.oispakaljaa.com/img/1024.png",
        "https://www.oispakalussa.tk/img/2048.png",
	"http://www.oispakaljaa.com/img/katko.png"

    ];
    for(var i = 0; i < imageList.length; i++ )
    {
        var imageObject = new Image();
        imageObject.src = imageList[i];
    }
