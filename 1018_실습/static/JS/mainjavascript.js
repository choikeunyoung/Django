// Movement Animation to happen
const card = document.querySelector('.card');
const container = document.querySelector('.container');

//Items
const title = document.querySelector('.title');
const item = document.querySelector('.item img');
const purchase = document.querySelector('.purchase button');
const description = document.querySelector('.info h3');
const options = document.querySelector('.options');

// Moving Animation Event
container.addEventListener("mousemove", (e) => {
    console.log(e.pageX, e.pageY);
    let xAxis = (window.innerWidth / 2 - e.pageX) / 20;
    let yAxis = (window.innerHeight / 2 - e.pageY) / 20;
    
    card.style.transform = `rotateY(${yAxis}deg) rotateX(${xAxis}deg)`
});

// Animate In
container.addEventListener('mouseenter', (e) => {
    card.style.transition = 'none';
    
    // Popout
    title.style.transform = 'translateZ(150px)';
    item.style.transform = 'translateZ(200px) rotateZ(-45deg)';
    description.style.transform = 'translateZ(125px)';
    options.style.transform = 'translateZ(100px)';
    purchase.style.transform = 'translateZ(75px)';
})

// Animate Out
container.addEventListener('mouseleave', e => {
    card.style.transition = 'all .3s ease';
    card.style.transform = `rotateY(0deg) rotateX(0deg)`

    // Popback
    title.style.transform = 'translateZ(0px)';
    item.style.transform = 'translateZ(0px) rotateZ(0)';
    description.style.transform = 'translateZ(0px)';
    options.style.transform = 'translateZ(0px)';
    purchase.style.transform = 'translateZ(0px)';
});