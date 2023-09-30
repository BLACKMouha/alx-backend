/* jshint esversion: 8 */

import { createClient } from "redis";

const client = createClient()
  .on('ready', (stream) => console.log('Redis client connected to the server'))
  .on('error', (e) => console.log('Redis client not connected to the server:', e));
