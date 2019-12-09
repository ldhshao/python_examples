import Model, {attr, hasMany} from '@ember-data/model';

export default Model.extend({
  fName: attr('string'),
  lName: attr('string'),
  email: attr('string'),
  signtings: hasMany('signting')
});
