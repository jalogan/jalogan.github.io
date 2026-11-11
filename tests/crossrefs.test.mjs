import test from 'node:test';
import assert from 'node:assert/strict';
import plugin from '../plugins/remarkScientificRefs.mjs';
const element=(name,id)=>({type:'mdxJsxFlowElement',name,attributes:[{type:'mdxJsxAttribute',name:'id',value:id}],children:[]});
test('numbers figures and video together, equations separately; rewrites refs',()=>{
 const root={type:'root', children:[element('FigRef','fig-two'),element('Figure','fig-one'),element('Equation','eq-one'),element('VideoFigure','fig-two'),element('EqRef','eq-one')]};
 plugin()(root,{path:'demo.mdx'});
 assert.equal(root.children[0].name,'a');
 assert.equal(root.children[0].children[0].value,'Figure 2');
 assert.equal(root.children[1].attributes.at(-1).value,'1');
 assert.equal(root.children[2].attributes.at(-1).value,'1');
 assert.equal(root.children[3].attributes.at(-1).value,'2');
 assert.equal(root.children[4].children[0].value,'Eq. (1)');
});
test('missing references fail the build',()=>{
 assert.throws(()=>plugin()({type:'root',children:[element('FigRef','fig-missing')]},{path:'example.mdx'}),/Unresolved FigRef/);
});
test('duplicate figure ids fail the build',()=>{
 assert.throws(()=>plugin()({type:'root',children:[element('Figure','fig-one'),element('Figure','fig-one')]},{path:'example.mdx'}),/Duplicate ID/);
});

test('one grouped scientific figure gets one number and its ID resolves',()=>{
 const root={type:'root',children:[element('FigureGroup','fig-multi'),element('FigRef','fig-multi'),element('Figure','fig-follow')]};
 plugin()(root,{path:'protein.mdx'});
 assert.equal(root.children[0].attributes.at(-1).value,'1');
 assert.equal(root.children[1].children[0].value,'Figure 1');
 assert.equal(root.children[2].attributes.at(-1).value,'2');
});


test('one grouped video figure gets one number and its ID resolves',()=>{
 const root={type:'root',children:[element('VideoGroup','fig-video-multi'),element('FigRef','fig-video-multi'),element('Figure','fig-follow')]};
 plugin()(root,{path:'manifold.mdx'});
 assert.equal(root.children[0].attributes.at(-1).value,'1');
 assert.equal(root.children[1].children[0].value,'Figure 1');
 assert.equal(root.children[2].attributes.at(-1).value,'2');
});
