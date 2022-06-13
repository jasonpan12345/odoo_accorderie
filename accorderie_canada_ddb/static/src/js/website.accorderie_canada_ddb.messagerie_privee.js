odoo.define('website.accorderie_canada_ddb.messagerie_privee.instance', function (require) {
    'use strict';

    require('web_editor.ready');
    let Messagerie = require('website.accorderie_canada_ddb.messagerie_privee');

    let $messagerie = $('.chat_box');
    if (!$messagerie.length) {
        return null;
    }

    let instance = new Messagerie();
    return instance.appendTo($messagerie).then(function () {
        return instance;
    });
});

//==============================================================================

odoo.define("website.accorderie_canada_ddb.messagerie_privee", function (require) {

    let ajax = require('web.ajax');
    let Widget = require('web.Widget');
    let chatBody = document.getElementsByClassName("chat_body");

    let Messagerie = Widget.extend({
        start: function () {
            let self = this;
            setInterval(function () {

                console.log("generate");
                let text = Math.floor(Math.random() * 2);
                if (text) {
                    self.generateMyText();
                } else {
                    self.generateTheirText();
                }
            }, 3000);

        },

        generateMyText: function () {
            // message text
            let newMessageBody = document.createElement("div");
            newMessageBody.className += "my_msg msg";
            let newMessageText = document.createTextNode(this.generateRandomMessage());
            newMessageBody.appendChild(newMessageText);

            // message time
            let newTime = document.createElement("div");
            newTime.className += "msg_time text-right";
            let newTimeText = document.createTextNode("3 semaines");
            newTime.appendChild(newTimeText);

            // message container
            let newMessage = document.createElement("div");
            newMessage.className += "chat_msg";
            newMessage.appendChild(newMessageBody);
            newMessage.appendChild(newTime);

            // add to chat-box
            chatBody[0].appendChild(newMessage);
        },

        generateTheirText: function () {
            // message text
            let newMessageBody = document.createElement("div");
            newMessageBody.className += "their_msg msg";
            let newMessageText = document.createTextNode(this.generateRandomMessage());
            newMessageBody.appendChild(newMessageText);

            // message time
            let newTime = document.createElement("div");
            newTime.className += "msg_time";
            let newTimeText = document.createTextNode("3 semaines");
            newTime.appendChild(newTimeText);

            // image
            let newImg = document.createElement("img");
            newImg.className += "contact_pic rounded-circle";
            newImg.src = "/web/image/accorderie_canada_ddb_website.ir_attachment_freestocks_9uvmlib0wju_unsplash_jpg/freestocks-9UVmlIb0wJU-unsplash.jpg";

            // message container
            let newMessage = document.createElement("div");
            newMessage.className += "chat_msg";
            newMessage.appendChild(newImg);
            newMessage.appendChild(newMessageBody);
            newMessage.appendChild(newTime);

            // add to chat-box
            chatBody[0].appendChild(newMessage);
        },

        generateRandomMessage: function () {
            let defaultText = "Lorem Ipsum ";
            let text="";

            for(let i = 0; i < Math.floor((Math.random() * 16)+1); i++) {
                text += defaultText;
            }

            return text;
        },
    });

    return Messagerie;
});