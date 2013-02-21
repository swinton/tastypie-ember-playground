# TastyPie-Ember-Playground

Demo of Ember.js used with TastyPie. In action at [http://tastypie-ember-playground.herokuapp.com/](http://tastypie-ember-playground.herokuapp.com/).

# Examples

## To create a record

```javascript
var user = App.User.find(1);
var msg = App.Message.createRecord({
    text: "A brand new message"
});
msg.set("user", user);
App.store.commit();
```

# Contact

@[steveWINton](http://twitter.com/steveWINton).
