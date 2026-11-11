import { existsSync } from 'node:fs';
import { join } from 'node:path';

// Place finalized public PDFs under public/docs/ using these filenames.
export const researchCvUrl = '/docs/jack-logan-research-cv.pdf';
export const industryResumeUrl = '/docs/jack-logan-industry-resume.pdf';
export const hasResearchCv = existsSync(join(process.cwd(), 'public', researchCvUrl.slice(1)));
export const hasIndustryResume = existsSync(join(process.cwd(), 'public', industryResumeUrl.slice(1)));
