function blink()
{
    let body = document.querySelector('body');
    
    if (body.style.visibility === 'hidden')
    {
        body.style.visibility = 'visible';
    }
    else
    {
        body.style.visibility = 'hidden';
    }
}

// call blink every 500ms
window.setInterval(blink, 500);