/**
 * Resolve local scientific figure/equation references before MDX compilation.
 * Numbering is independent on each article and includes videos in the Figure sequence.
 * Build fails for missing or duplicate IDs and non-literal IDs.
 * Example: <Figure id="fig-demo" .../> and <FigRef id="fig-demo"/>.
 */
function walk(node, fn) {
  if (!node || typeof node !== 'object') return;
  fn(node);
  for (const child of node.children || []) walk(child, fn);
}
function literalAttr(node, key) {
  const attr = (node.attributes || []).find((a) => a.type === 'mdxJsxAttribute' && a.name === key);
  return typeof attr?.value === 'string' ? attr.value : null;
}
function addAttr(node, name, value) {
  node.attributes ??= [];
  if (node.attributes.some(a => a.name === name)) throw new Error(`Do not set ${name} manually: it is generated.`);
  node.attributes.push({ type: 'mdxJsxAttribute', name, value: String(value) });
}
export default function remarkScientificRefs() {
  return (tree, file = {}) => {
    const figureIds = new Map();
    const equationIds = new Map();
    let figures = 0, equations = 0;
    let nodeIndex = 0;
    const errors = [];
    walk(tree, (node) => {
      if (!['mdxJsxFlowElement', 'mdxJsxTextElement'].includes(node.type)) return;
      if (!['Figure', 'FigureGroup', 'VideoFigure', 'VideoGroup', 'Equation'].includes(node.name)) return;
      const id = literalAttr(node, 'id');
      if (!id) { errors.push(`<${node.name}> must have a literal id="..."`); return; }
      if (!/^(fig|eq)-[a-z0-9-]+$/.test(id)) { errors.push(`Invalid ID: ${id}`); return; }
      if (figureIds.has(id) || equationIds.has(id)) { errors.push(`Duplicate ID: ${id}`); return; }
      if (node.name === 'Equation') {
        if (!id.startsWith('eq-')) errors.push(`Equation IDs must begin eq-: ${id}`);
        equationIds.set(id, ++equations); addAttr(node, 'number', equations);
      } else {
        if (!id.startsWith('fig-')) errors.push(`Figure IDs must begin fig-: ${id}`);
        figureIds.set(id, ++figures); addAttr(node, 'number', figures);
      }
      nodeIndex++;
    });
    walk(tree, (node) => {
      if (!['mdxJsxFlowElement', 'mdxJsxTextElement'].includes(node.type)) return;
      if (!['FigRef', 'EqRef'].includes(node.name)) return;
      const id = literalAttr(node, 'id');
      const isFigure = node.name === 'FigRef';
      const number = (isFigure ? figureIds : equationIds).get(id);
      if (!number) { errors.push(`Unresolved ${node.name} id="${id ?? 'missing'}"`); return; }
      node.name = 'a';
      node.attributes = [{type:'mdxJsxAttribute', name:'href', value:`#${id}`}];
      node.children = [{type:'text', value: isFigure ? `Figure ${number}` : `Eq. (${number})`}];
    });
    if (errors.length) throw new Error(`Scientific cross-reference error in ${file.path || 'MDX file'}:\n${errors.join('\n')}`);
  };
}
