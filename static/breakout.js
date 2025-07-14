window.onload = function() {
    drawObjects()
}


function drawObjects() {
for (let i = 0; i < 80; i++) {
    let blocks = document.createElement('img');
    blocks.id = i.toString();
    if (i % 2 == 0) {
        blocks.src = "RedBlock.png"
        blocks.className = "Even"
    } else {
        blocks.src = "OrangeBlock.png"
        blocks.className = "Odd"
    }
    document.getElementById("enemyBlocks").appendChild(blocks);
    }

}

let player = document.createElement('img');
player.id = "playerSprite";
player.src = "player.png";
document.getElementById('playerField').appendChild(player);

document.getElementById("playingField").addEventListener('mousemove', (event) => {
    const mouseX = event.pageX;

    player.style.left = mouseX + 'px';
});

let ball = document.createElement('img');
ball.src = "ball.png"
/*document.getElementById('playingField').appendChild(ball)*/
let ballx = 0, bally = 0;
const speed = 40;

function moveBall() {
    ballx += speed;
    bally += speed;

    ball.style.left = x + "px";
    ball.style.top = y + "px";

    requestAnimationFrame(moveBall)
}

moveBall();