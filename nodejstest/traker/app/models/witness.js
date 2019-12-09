import Model, {attr, hasMany} from '@ember-data/model';
import Ember from '@ember'

export default Model.extend({
  fName: attr('string'),
  lName: attr('string'),
  email: attr('string'),
  signtings: hasMany('signting'),
  fullName: Ember.computed('fName', 'lName', function(){
    return this.get('fName') + ' ' + this.get('lName');
  })
});
