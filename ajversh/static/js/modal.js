$('.dropdown')
    .dropdown({
        action: 'hide'
    })
;

$('.ui.basic.modal')
    .modal('attach events', '.quit', 'show')
;

$('.ui.modal.info')
    .modal('setting', 'closable', true)
    .modal('attach events', '.link', 'show')
;

$('.ui.accordion')
    .accordion();