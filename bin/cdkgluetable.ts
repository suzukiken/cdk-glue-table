#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { CdkgluetableStack } from '../lib/cdkgluetable-stack';

const app = new cdk.App();
new CdkgluetableStack(app, 'CdkgluetableStack');
