/* global defineEventHandler, useRuntimeConfig */
/* eslint no-console: ["error", { allow: ["warn","debug","error"] }] */

import { createError, readBody, appendHeader } from 'h3'

export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig()
  if (!config.public.apiBase) {
    throw new Error('Missing `runtimeConfig.apiBase` configuration.')
  }
  const { method, url, headers } = event.req
  const body = method !== 'GET' && method !== 'HEAD' ? await readBody(event) : undefined
  console.debug('API MIDDLEWARE', { method, url, headers })

  try {
    const response = await $fetch.raw(url, {
      method,
      baseURL: config.public.apiBase,
      headers,
      body
    })

    for (const header of ['set-cookie', 'cache-control']) {
      if (response.headers.has(header)) {
        appendHeader(event, header, response.headers.get(header))
      }
    }
    console.log(`RESPONSE._data for ${url}`, response._data)
    return response._data
  } catch (error) {
    return createError({
      statusCode: error.response.status,
      statusMessage: error.message,
      data: error.data
    })
  }
})
