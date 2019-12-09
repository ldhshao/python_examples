import Model, {attr, hasMany} from '@ember-data/model';

export default Model.extend({
  name: attr('string'),
  cryptidType: attr('string'),
  profileImg: attr('string'),
  signtings: hasMany('signting')
});
