function f_color() {
    var rekomen = document.getElementsByClassName("rekomendasi");
    for (var i = 0; i < rekomen.length; ++i) {
        if (rekomen[i].innerHTML   == "Very Recommended") { 
            rekomen[i] .style.color = "rgb(35, 170, 22)";
         }else if (rekomen[i] .innerHTML == 'Recommended') {
            rekomen[i] .style.color = "rgb(31, 107, 250)" ;
         } else{
            rekomen[i] .style.color = "rgb(245, 62, 62)";
         }
    }
    
    
    };
    
f_color();