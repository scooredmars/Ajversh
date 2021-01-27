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

$('.ui.modal.list')
    .modal('attach events', '.add-item', 'show')
;

$('.ui.accordion')
    .accordion();