function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function moreInfo(buildId){
    fetch(url, {
        method:'POST',
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'buildId':buildId})
    })
    .then((resp) => resp.json())
    .then(function(data) {
        $(".txt").remove();
        $(".left-imgs").remove();
        $(".header").append('<div class="txt">' + data.name + ' (' + data.role +')<div class="actions remove-btn"><i class="cancel remove-btn icon"></i></div></div>');
        $(".description").prepend('<div class="left-imgs"></div>');
        $(".left-imgs").append('<img src="' + data.head_img + '" title="' + data.head + '" width="100px" style="position: absolute; top: 116px; left: 190px;">');
        $(".left-imgs").append('<img src="' + data.chest_img + '" title="' + data.chest + '" width="100px" style="position: absolute; top: 227px; left: 190px;">');
        $(".left-imgs").append('<img src="' + data.boots_img + '" title="' + data.boots + '" width="100px" style="position: absolute; top: 339px; left: 190px;">');
        $(".left-imgs").append('<img src="' + data.hand_img + '" title="' + data.hand + '" width="100px" style="position: absolute; top: 227px; left: 62px;">');
        if (data.off_hand_img != undefined ) {
            $(".left-imgs").append('<img src="' + data.off_hand_img + '" title="' + data.off_hand + '" width="100px" style="position: absolute; top: 227px; left: 320px;">');
        }

        $(".preview-head").remove();
        $(".right-data").append('<div class="item preview-head"></div>');
        $(".preview-head").append('<div class="category">Głowa</div>');
        $(".preview-head").append('<div class="item-info head">' + data.head + '</div>');
        $(".preview-head").append('<div class="item-img head-img"><img class="item-build" src="' + data.head_img + '" title="' + data.head + '"></div>');
        $(".head-img").append('<img class="spell" src="' + data.head_spell + '" title="' + data.head_spell_name + '">');
        $(".head-img").append('<img class="spell" src="' + data.head_pasive + '" title="' + data.head_pasive_name + '">');

        $(".preview-chest").remove();
        $(".right-data").append('<div class="item preview-chest"></div>');
        $(".preview-chest").append('<div class="category">Klata</div>');
        $(".preview-chest").append('<div class="item-info chest">' + data.chest + '</div>');
        $(".preview-chest").append('<div class="item-img chest-img"><img class="item-build" src="' + data.chest_img + '" title="' + data.chest + '"></div>');
        $(".chest-img").append('<img class="spell" src="' + data.chest_spell + '" title="' + data.chest_spell_name + '">');
        $(".chest-img").append('<img class="spell" src="' + data.chest_pasive + '" title="' + data.chest_pasive_name + '">');
        if (data.chest_pasive_tank != undefined) {
            $(".chest-img").append('<img class="spell" src="' + data.chest_pasive_tank + '" title="' + data.chest_pasive_tank_name + '">');
        }

        $(".preview-boots").remove();
        $(".right-data").append('<div class="item preview-boots"></div>');
        $(".preview-boots").append('<div class="category">Buty</div>');
        $(".preview-boots").append('<div class="item-info boots">' + data.boots + '</div>');
        $(".preview-boots").append('<div class="item-img boots-img"><img class="item-build" src="' + data.boots_img + '" title="' + data.boots + '"></div>');
        $(".boots-img").append('<img class="spell" src="' + data.boots_spell + '" title="' + data.boots_spell_name + '">');
        $(".boots-img").append('<img class="spell" src="' + data.boots_pasive + '" title="' + data.boots_pasive_name + '">');

        $(".preview-weapon").remove();
        $(".right-data").append('<div class="item preview-weapon"></div>');
        $(".preview-weapon").append('<div class="category">Broń Główna</div>');
        $(".preview-weapon").append('<div class="item-info weapon">' + data.hand + '</div>');
        $(".preview-weapon").append('<div class="item-img weapon-img"><img class="item-build" src="' + data.hand_img + '" title="' + data.hand + '"></div>');
        $(".weapon-img").append('<img class="spell" src="' + data.hand_q_img + '" title="' + data.hand_q + '">');
        $(".weapon-img").append('<img class="spell" src="' + data.hand_w_img + '" title="' + data.hand_w + '">');
        $(".weapon-img").append('<img class="spell" src="' + data.hand_e_img + '" title="' + data.hand_e + '">');
        $(".weapon-img").append('<img class="spell" src="' + data.hand_pasive_img + '" title="' + data.hand_pasive + '">');

        if (data.off_hand_img != undefined ) {
            $(".preview-second-weapon").remove();
            $(".right-data").append('<div class="item preview-second-weapon"></div>');
            $(".preview-second-weapon").append('<div class="category">Broń Poboczna</div>');
            $(".preview-second-weapon").append('<div class="item-info sec-weapon">' + data.off_hand + '</div>');
            $(".preview-second-weapon").append('<div class="item-img sec-weapon-img"><img class="item-build" src="' + data.off_hand_img + '" title="' + data.off_hand + '"></div>');
        }
        else {
            $(".preview-second-weapon").remove();
        }
    })
}