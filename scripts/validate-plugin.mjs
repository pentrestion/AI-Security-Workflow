import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const checks = [];

const assertExists = (relPath) => {
  const full = path.join(root, relPath);
  const exists = fs.existsSync(full);
  checks.push({ relPath, exists });
  if (!exists) {
    console.error(`Missing required file: ${relPath}`);
  }
};

assertExists('.claude-plugin/plugin.json');
assertExists('.mcp.json');
assertExists('CLAUDE.md');
assertExists('skills/web-testing/SKILL.md');
assertExists('skills/iot-testing/SKILL.md');
assertExists('skills/supply-chain-testing/SKILL.md');
assertExists('skills/network-testing/SKILL.md');
assertExists('skills/reverse-engineering/SKILL.md');
assertExists('skills/library-testing/SKILL.md');

const pluginJson = JSON.parse(fs.readFileSync(path.join(root, '.claude-plugin/plugin.json'), 'utf8'));
const allowedKeys = ['name', 'version', 'description', 'author'];
const extraKeys = Object.keys(pluginJson).filter((key) => !allowedKeys.includes(key));
if (extraKeys.length > 0) {
  console.error(`plugin.json contains unsupported keys: ${extraKeys.join(', ')}`);
  process.exit(1);
}

if (!pluginJson.name || !pluginJson.version || !pluginJson.description || !pluginJson.author) {
  console.error('plugin.json is missing required fields.');
  process.exit(1);
}

const failed = checks.filter((entry) => !entry.exists);
if (failed.length > 0) {
  process.exit(1);
}

console.log('Plugin structure validated successfully.');
