$('form input[type="file"]').change(event => {
    let files = event.target.files;
    if (files.length === 0) {
      console.log('sem image pra mostrar')
    } else {
        if(files[0].type == 'image/jpeg') {
          $('img').remove();
          let image = $('<img class="img-responsive">');
          image.attr('src', window.URL.createObjectURL(files[0]));
          $('figure').prepend(image);
        } else {
          alert('Formato não suportado')
        }
    }
  });