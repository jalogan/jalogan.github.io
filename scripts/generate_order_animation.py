"""Reproducible visual study: relaxational dynamics of a coarse-grained complex
sixfold orientational order parameter, psi_6.

Model-A dynamics from F = integral ( -a|psi|^2/2 + b|psi|^4/4
                                   + kappa|grad psi|^2/2 ) dA.
  dpsi/dt = Gamma*(a*psi - b*|psi|^2*psi + kappa*Laplacian psi).

NOTE: a phenomenological order-parameter model, NOT MD of interacting polygons
or the published SymBOPs implementation. No hand-animated hue shifts.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
import numpy as np
from scipy.ndimage import gaussian_filter
from PIL import Image, ImageEnhance

HERE=Path(__file__).resolve().parent.parent
DEST=HERE/'public'/'art'
DEST.mkdir(parents=True,exist_ok=True)
# Initialize from actual neighbor-computed psi_6 values in the earlier D study.
# Dataset: passive tracers in a simulated 2D vortex flow; NOT hard-polygon MD.
from scipy.ndimage import gaussian_filter
DATA=HERE/'data'/'initial-tracer-bond-order.npz'
z=np.load(DATA)
xy=z['pos']; q=z['q6']; LX=float(z['W']); LY=float(z['H'])
NY,NX=264,528
edges_x=np.linspace(0,LX,NX+1)
edges_y=np.linspace(0,LY,NY+1)
density=np.histogram2d(xy[:,0],xy[:,1],bins=[edges_x,edges_y])[0].T
real=np.histogram2d(xy[:,0],xy[:,1],bins=[edges_x,edges_y],weights=q.real)[0].T
imag=np.histogram2d(xy[:,0],xy[:,1],bins=[edges_x,edges_y],weights=q.imag)[0].T
sig=3.3
psi=(gaussian_filter(real,sig,mode='wrap')+1j*gaussian_filter(imag,sig,mode='wrap'))/(gaussian_filter(density,sig,mode='wrap')+1e-7)
psi=np.clip(abs(psi),0,1)*np.exp(1j*np.angle(psi))
kx=2*np.pi*np.fft.fftfreq(NX,d=LX/NX)[None,:]
ky=2*np.pi*np.fft.fftfreq(NY,d=LY/NY)[:,None]
k2=kx*kx+ky*ky
# Relaxational Model-A dynamics for the coarse-grained sixfold field. The
# dynamically changing colors are derived from psi_6, not animated gradients.
A=1.0;B=1.0;KAPPA=.0075;GAMMA=.18;DT=.070
# Gentle looping design: hold initial state ~4 s, then evolve for a longer
# physical interval at the V6 simulation and playback rates, before reversing. The backward segment is editorial playback,
# not time-reversible dynamics. The underlying forward states solve the PDE.
frames=118
steps_per_frame=2
FPS=18
HOLD_START=72
HOLD_END=7
palette=['#6848ba','#3479d8','#49bdc6','#f2c978','#f18966','#df70a5','#6848ba']
colors=np.array([[int(c[j:j+2],16) for j in (1,3,5)] for c in palette],float)
white=np.array([250,250,246.],float)

def draw(z):
    angle=(np.angle(z)/(2*np.pi)+.56)%1
    t=angle*(len(colors)-1)
    idx=np.floor(t).astype('int32')
    f=(t-idx)[:,:,None]
    rgb=colors[idx]*(1-f)+colors[idx+1]*f
    order=np.clip(abs(z),0,1)
    # order amplitude controls saturation/opacity; coherent regions develop color.
    strength=(.31+.63*(order**.8))[:,:,None]
    rgb=rgb*strength+white*(1-strength)
    # Apply mild white canvas lightening at edge to avoid harsh cutoffs.
    return Image.fromarray(np.uint8(np.clip(rgb,0,255)),'RGB').resize((960,480),Image.Resampling.BICUBIC)

def step(z):
    nonlinear=(A*z-B*abs(z)**2*z)
    return np.fft.ifft2((np.fft.fft2(z)+DT*GAMMA*np.fft.fft2(nonlinear)) /
                        (1+DT*GAMMA*KAPPA*k2))

# Encode from streamed RGB frames instead of writing hundreds of temporary PNGs.
# This preserves reproducibility while keeping generation practical on laptops.
source=[]
for j in range(frames):
    if j > 0:
        for _ in range(steps_per_frame):
            psi=step(psi)
    source.append(np.asarray(draw(psi),dtype=np.uint8).tobytes())
Image.frombytes('RGB',(960,480),source[0]).save(DEST/'ordering-poster.webp',quality=85,method=6)
Image.frombytes('RGB',(960,480),source[-1]).save(DEST/'ordering-last-frame.webp',quality=82,method=6)
all_indices=([0]*HOLD_START + list(range(1,frames)) +
             [frames-1]*HOLD_END + list(range(frames-2,-1,-1)))

def encode(path,codec_args):
    cmd=['ffmpeg','-y','-v','error','-f','rawvideo','-pixel_format','rgb24',
         '-video_size','960x480','-framerate',str(FPS),'-i','pipe:0',
         '-an',*codec_args,str(path)]
    with subprocess.Popen(cmd,stdin=subprocess.PIPE) as proc:
        try:
            for idx in all_indices:
                proc.stdin.write(source[idx])
        except BrokenPipeError as exc:
            raise RuntimeError(f'ffmpeg failed to encode {path}') from exc
        finally:
            proc.stdin.close()
        if proc.wait()!=0:
            raise RuntimeError(f'ffmpeg failed to encode {path}')

mp4=DEST/'order-evolution.mp4'
webm=DEST/'order-evolution.webm'
encode(mp4,['-c:v','libx264','-preset','veryfast','-crf','27',
            '-pix_fmt','yuv420p','-movflags','+faststart'])
encode(webm,['-c:v','libvpx-vp9','-deadline','realtime','-cpu-used','8',
             '-b:v','0','-crf','36','-pix_fmt','yuv420p'])
print('generated',len(all_indices),'frames',round(len(all_indices)/FPS,2),'seconds',
      [(p.name,round(p.stat().st_size/1024)) for p in
       [mp4,webm,DEST/'ordering-poster.webp']])
