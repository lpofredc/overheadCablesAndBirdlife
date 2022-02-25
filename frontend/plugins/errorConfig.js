/**
 * This file contains the errorcode configuration for the app.
 *
 * code: it is error code determined for this app.
 * Values start at 601 to avoid confusion with HTTP statusCodes.
 * Error capture in nuxt do not contains "statusError" property, only "message" property
 * This "message" property is not provided to user.
 *
 * msg: it is message provided when the error occures. The chain matches to chain used by i18n
 * (internationalization). Refer in '~/locales/*'.
 */
errorCodes = {
  // refer loadNomenclatures in nomenclatureStore
  loading_whole_nomenclatures: {
    code: 601,
    msg: 'loading-issue',
  },
  // refer getConditions in nomenclatureStore
  get_infrstr_conditions: {
    code: 602,
    msg: 'loading-issue',
  },
  // refer getOwners in nomenclatureStore
  get_infrstr_owners: {
    code: 603,
    msg: 'loading-issue',
  },
  // refer getPoleTypes in nomenclatureStore
  get_infrstr_poletypes: {
    code: 604,
    msg: 'loading-issue',
  },
  // refer getPoleTypes in nomenclatureStore
  get_infrstr_risklevels: {
    code: 605,
    msg: 'loading-issue',
  },
  // refer submit in point-component
  create_pole: {
    code: 701,
    msg: 'create-issue',
  },
}
